(SELECT * FROM dash_tracker_ingradient
LEFT OUTER JOIN
    (SELECT name AS ingradient_name, id
    FROM dash_tracker_ingradientname
    WHERE dash_tracker_ingradientname.lang_id =
        (SELECT lang_id
        FROM dash_tracker_profile
        WHERE user_id = %s)
    )
AS dash_tracker_ingradientname
ON dash_tracker_ingradientname.id = dash_tracker_ingradient.id
)
LEFT OUTER JOIN
    (SELECT name AS mesurement_name, id
    FROM dash_tracker_mesurementname
    WHERE dash_tracker_mesurementname.lang_id =
        (SELECT lang_id
        FROM dash_tracker_profile
        WHERE user_id = %s)
     )
AS dash_tracker_mesurementname
ON dash_tracker_mesurementname.id = dash_tracker_mesurement.id