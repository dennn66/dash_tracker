from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Language, ProductTypeName, ProductGroupName, Mesurement, MesurementName, \
    Ingradient,IngradientName, Meal, MealName, ProductItem, Profile
from .forms import ProductItemForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

@login_required
def product_list(request):

    product_items = ProductItem.objects.raw('SELECT * FROM dash_tracker_productitem '
                                            'LEFT OUTER JOIN '
                                     '  (SELECT name AS ingradient_name, id '
                                     '  FROM dash_tracker_ingradientname '
                                     '  WHERE dash_tracker_ingradientname.lang_id = ('
                                     '      SELECT lang_id '
                                     '      FROM dash_tracker_profile '
                                     '      WHERE user_id = %s)) '
                                     'AS dash_tracker_ingradientname '
                                     'ON dash_tracker_ingradientname.id = dash_tracker_productitem.ingradient_id '
                                      'LEFT OUTER JOIN (' 
                                       'SELECT name ' 
                                       'AS mesurement_name, id ' 
                                       'FROM dash_tracker_mesurementname ' 
                                       'WHERE dash_tracker_mesurementname.lang_id = (' 
                                       'SELECT lang_id ' 
                                       'FROM dash_tracker_profile ' 
                                       'WHERE user_id = %s)) ' 
                                       'AS dash_tracker_mesurementname ' 
                                       'ON dash_tracker_mesurementname.id = dash_tracker_productitem.mesurement_id '
                                        ' LEFT OUTER JOIN ('
                                        ' SELECT name'
                                        ' AS meal_name, id'
                                        ' FROM dash_tracker_mealname'
                                        ' WHERE dash_tracker_mealname.lang_id = ('
                                        ' SELECT lang_id'
                                        ' FROM dash_tracker_profile'
                                        ' WHERE user_id = %s))'
                                        ' AS dash_tracker_mealname '
                                        ' ON dash_tracker_mealname.id = dash_tracker_productitem.meal_id  '
                                            ,
                                       [request.user.id, request.user.id, request.user.id])


    for product_item in product_items:
        print(product_item)
    return render(request, 'dash_tracker/product_list.html', {'product_items': product_items})

@login_required
def product_new(request):
    if request.method == "POST":
        form = ProductItemForm(request.POST)
        if form.is_valid():
            product_item = form.save(commit=False)
            product_item.user = request.user
            product_item.save()
            return redirect('product_detail', pk=product_item.pk)
    else:
        form = ProductItemForm()
    return render(request, 'dash_tracker/product_edit.html', {'form': form})

@login_required
def product_detail(request, pk):
    product_item = get_object_or_404(ProductItem, pk=pk)
    return render(request, 'dash_tracker/product_detail.html', {'product_item': product_item})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(ProductItem, pk=pk)
    if request.method == "POST":
        form = ProductItemForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductItemForm(instance=product)
    return render(request, 'dash_tracker/product_edit.html', {'form': form})