#Answer business questions

#In relation to the products:

#What categories of tech products does Magist have?
	SELECT 
		product_category_name_english
	FROM
		products AS p
			LEFT JOIN
		product_category_name_translation AS translation ON p.product_category_name = translation.product_category_name
	GROUP BY product_category_name_english;

#Tech categories are
#'air_conditioning'
#'audio'
#'cds_dvds_musicals'
#'cine_photo'
#'computers'
#'computers_accessories'
#'consoles_games'
#'dvds_blu_ray'
#'electronics'
#'fixed_telephony'
#'home_appliances'
#'home_appliances_2'
#'music'
#'musical_instruments'
#'portable_kitchen_food_processors'
#'pc_gamer'
#'security_and_services'
#'signaling_and_security'
#'small_appliances'
#'small_appliances_home_oven_and_coffee'
#'tablets_printing_image'
#'telephony'
#'watches_gifts'

SELECT 
    product_category_name_english
FROM
    products AS p
        LEFT JOIN
    product_category_name_translation AS translation ON p.product_category_name = translation.product_category_name
WHERE product_category_name_english IN ('air_conditioning','audio','cds_dvds_musicals','cine_photo','computers','computers_accessories','consoles_games','dvds_blu_ray','electronics','fixed_telephony','home_appliances','home_appliances_2','music','musical_instruments','portable_kitchen_food_processors','pc_gamer','security_and_services','signaling_and_security','small_appliances','small_appliances_home_oven_and_coffee','tablets_printing_image','telephony','watches_gifts')
GROUP BY product_category_name_english;


# How many products of these tech categories have been sold (within the time window of the database snapshot)? 
	# I consider as sold products those that has been delievered, shipped or approved in the order table.
	# Then I have to make a many to many join between products and orders through order_items
	SELECT 
		transl.product_category_name_english AS category,
		COUNT(product_category_name_english) AS n_sold
	FROM
		order_items AS oi
			LEFT JOIN
		products AS p ON p.product_id = oi.product_id
			LEFT JOIN
		orders AS o ON o.order_id = oi.order_id
			LEFT JOIN
		product_category_name_translation AS transl ON p.product_category_name = transl.product_category_name
	WHERE
		product_category_name_english IN ('air_conditioning' , 'audio',
			'cds_dvds_musicals',
			'cine_photo',
			'computers',
			'computers_accessories',
			'consoles_games',
			'dvds_blu_ray',
			'electronics',
			'fixed_telephony',
			'home_appliances',
			'home_appliances_2',
			'music',
			'musical_instruments',
			'portable_kitchen_food_processors',
			'pc_gamer',
			'security_and_services',
			'signaling_and_security',
			'small_appliances',
			'small_appliances_home_oven_and_coffee',
			'tablets_printing_image',
			'telephony',
			'watches_gifts')
			AND o.order_status IN ('delivered' , 'shipped', 'approved')
	GROUP BY category
	ORDER BY n_sold DESC;

#What percentage does that represent from the overall number of products sold?
	#Below I calculate the total number of tech products
	SELECT 
		count(o.order_id)
	FROM
		order_items AS oi
			LEFT JOIN
		products AS p ON p.product_id = oi.product_id
			LEFT JOIN
		orders AS o ON o.order_id = oi.order_id
			LEFT JOIN
		product_category_name_translation AS transl ON p.product_category_name = transl.product_category_name
	WHERE
		product_category_name_english IN ('air_conditioning' , 'audio',
			'cds_dvds_musicals',
			'cine_photo',
			'computers',
			'computers_accessories',
			'consoles_games',
			'dvds_blu_ray',
			'electronics',
			'fixed_telephony',
			'home_appliances',
			'home_appliances_2',
			'music',
			'musical_instruments',
			'portable_kitchen_food_processors',
			'pc_gamer',
			'security_and_services',
			'signaling_and_security',
			'small_appliances',
			'small_appliances_home_oven_and_coffee',
			'tablets_printing_image',
			'telephony',
			'watches_gifts')
			AND o.order_status IN ('delivered' , 'shipped', 'approved');

	#Below I calculate the total number of any sort

	SELECT 
		COUNT(o.order_id)
	FROM
		order_items AS oi
			LEFT JOIN
		products AS p ON p.product_id = oi.product_id
			LEFT JOIN
		orders AS o ON o.order_id = oi.order_id
			LEFT JOIN
		product_category_name_translation AS transl ON p.product_category_name = transl.product_category_name
	WHERE
		o.order_status IN ('delivered' , 'shipped', 'approved');
    
	SELECT(25985/111385*100);
    # x = (25985/111385)*100 ~23.3%

#What’s the average price of the products being sold?
	SELECT 
		transl.product_category_name_english AS category,
		COUNT(product_category_name_english) AS n_sold,
		ROUND(AVG(oi.price)) AS avg_price
	FROM
		order_items AS oi
			LEFT JOIN
		products AS p ON p.product_id = oi.product_id
			LEFT JOIN
		orders AS o ON o.order_id = oi.order_id
			LEFT JOIN
		product_category_name_translation AS transl ON p.product_category_name = transl.product_category_name
	WHERE
		product_category_name_english IN ('air_conditioning' , 'audio',
			'cds_dvds_musicals',
			'cine_photo',
			'computers',
			'computers_accessories',
			'consoles_games',
			'dvds_blu_ray',
			'electronics',
			'fixed_telephony',
			'home_appliances',
			'home_appliances_2',
			'music',
			'musical_instruments',
			'portable_kitchen_food_processors',
			'pc_gamer',
			'security_and_services',
			'signaling_and_security',
			'small_appliances',
			'small_appliances_home_oven_and_coffee',
			'tablets_printing_image',
			'telephony',
			'watches_gifts')
			AND o.order_status IN ('delivered' , 'shipped', 'approved')
	GROUP BY category
	ORDER BY n_sold DESC;

#Are expensive tech products popular?
	#I introduce 4 categories x<€50: super cheap 50<x<150 cheap 150<x<400 expensive x>400 super expensive
	SELECT 
		transl.product_category_name_english AS category,
		COUNT(product_category_name_english) AS n_sold,
		ROUND(AVG(oi.price)) AS avg_price,
		CASE
			WHEN ROUND(AVG(oi.price))  > 400 THEN 'expensive'
			ELSE 'cheap'
		END AS cost
	FROM
		order_items AS oi
			LEFT JOIN
		products AS p ON p.product_id = oi.product_id
			LEFT JOIN
		orders AS o ON o.order_id = oi.order_id
			LEFT JOIN
		product_category_name_translation AS transl ON p.product_category_name = transl.product_category_name
	WHERE
		product_category_name_english IN ('air_conditioning' , 'audio',
			'cds_dvds_musicals',
			'cine_photo',
			'computers',
			'computers_accessories',
			'consoles_games',
			'dvds_blu_ray',
			'electronics',
			'fixed_telephony',
			'home_appliances',
			'home_appliances_2',
			'music',
			'musical_instruments',
			'portable_kitchen_food_processors',
			'pc_gamer',
			'security_and_services',
			'signaling_and_security',
			'small_appliances',
			'small_appliances_home_oven_and_coffee',
			'tablets_printing_image',
			'telephony',
			'watches_gifts')
			AND o.order_status IN ('delivered' , 'shipped', 'approved')
	GROUP BY category
	ORDER BY n_sold DESC;



#3.2. In relation to the sellers:

#How many months of data are included in the magist database?
	#I focus on the orders database where we have dates
    #In particular I focus on the order_approved_at column
	
    SELECT 
		YEAR(order_approved_at) AS year,
		COUNT(DISTINCT MONTH(order_approved_at)) AS n_month
	FROM
		orders
	GROUP BY year;



#How many sellers are there? 
	SELECT 
		count(DISTINCT seller_id)
	FROM
		sellers;
	
    #There are 3095 sellers
    
#How many Tech sellers are there? What percentage of overall sellers are Tech sellers?
	#To answer this question we need to join the seller table with the products one
        
    SELECT
		count(DISTINCT oi.seller_id) AS n_sellers
	FROM
		order_items AS oi
			LEFT JOIN
		sellers AS s ON s.seller_id = oi.seller_id
			LEFT JOIN
		products AS p ON p.product_id = oi.product_id
			LEFT JOIN
		product_category_name_translation AS transl ON p.product_category_name = transl.product_category_name
	WHERE
    product_category_name_english IN ('air_conditioning' , 'audio',
        'cds_dvds_musicals',
        'cine_photo',
        'computers',
        'computers_accessories',
        'consoles_games',
        'dvds_blu_ray',
        'electronics',
        'fixed_telephony',
        'home_appliances',
        'home_appliances_2',
        'music',
        'musical_instruments',
        'portable_kitchen_food_processors',
        'pc_gamer',
        'security_and_services',
        'signaling_and_security',
        'small_appliances',
        'small_appliances_home_oven_and_coffee',
        'tablets_printing_image',
        'telephony',
        'watches_gifts');
        
    
	#There is a total of 3095 sellers 790 of which are tech sellers. This is ~ 25.5%
    
    
    
    
    
    

#What is the total amount earned by all sellers? What is the total amount earned by all Tech sellers?
	#Here we need to join with the orders table because there is the order_status
    #Then we will compute the income by summing the price in order_items
    
	SELECT 
		ROUND(SUM(oi.price)-SUM(oi.freight_value)) AS total_income
	FROM
		order_items AS oi
			LEFT JOIN
		sellers AS s ON s.seller_id = oi.seller_id
			LEFT JOIN
		products AS p ON p.product_id = oi.product_id
			LEFT JOIN
		product_category_name_translation AS transl ON p.product_category_name = transl.product_category_name
			LEFT JOIN
		orders AS o ON o.order_id = oi.order_id
	WHERE o.order_status IN ('delivered' , 'shipped', 'approved')
    AND product_category_name_english IN ('air_conditioning' , 'audio',
        'cds_dvds_musicals',
        'cine_photo',
        'computers',
        'computers_accessories',
        'consoles_games',
        'dvds_blu_ray',
        'electronics',
        'fixed_telephony',
        'home_appliances',
        'home_appliances_2',
        'music',
        'musical_instruments',
        'portable_kitchen_food_processors',
        'pc_gamer',
        'security_and_services',
        'signaling_and_security',
        'small_appliances',
        'small_appliances_home_oven_and_coffee',
        'tablets_printing_image',
        'telephony',
        'watches_gifts');

	#The total income for all the sellers is €11147726 and for the tech sellers is €3265246. This is the ~ 29.3%
SELECT(3265246/11147726*100);

#Can you work out the average monthly income of all sellers? Can you work out the average monthly income of Tech sellers?
	#As done before we consider as date the order_approved_at column
    #In the previous analysis we have seen that the year 2017 is the only with 12 effective months
    #Therefore, we will restrict to that year to extract the monthly avg
	SELECT 
		ROUND(AVG(oi.price))
	FROM
		order_items AS oi
			LEFT JOIN
		sellers AS s ON s.seller_id = oi.seller_id
			LEFT JOIN
		products AS p ON p.product_id = oi.product_id
			LEFT JOIN
		product_category_name_translation AS transl ON p.product_category_name = transl.product_category_name
			LEFT JOIN
		orders AS o ON o.order_id = oi.order_id
	WHERE o.order_status IN ('delivered' , 'shipped', 'approved')
		AND YEAR(o.order_approved_at) = 2017
		AND product_category_name_english IN ('air_conditioning' , 'audio',
        'cds_dvds_musicals',
        'cine_photo',
        'computers',
        'computers_accessories',
        'consoles_games',
        'dvds_blu_ray',
        'electronics',
        'fixed_telephony',
        'home_appliances',
        'home_appliances_2',
        'music',
        'musical_instruments',
        'portable_kitchen_food_processors',
        'pc_gamer',
        'security_and_services',
        'signaling_and_security',
        'small_appliances',
        'small_appliances_home_oven_and_coffee',
        'tablets_printing_image',
        'telephony',
        'watches_gifts');
	
    # The monthly average income of all sellers is €118
    # Those of non tech sellers is €156
    -- Sarra's code
    SELECT 
		(SUM(price) - SUM(freight_value)) / (TIMESTAMPDIFF(MONTH,
			MIN(order_purchase_timestamp),
			MAX(order_purchase_timestamp))) AS avg_monthly_earnings
	FROM
		order_items
			LEFT JOIN
    orders USING (order_id);
	
    -- Risto's code
    SELECT 
    (SELECT 
            ROUND(SUM(o.price) / 25)
        FROM
            sellers s
                INNER JOIN
            order_items o USING (seller_id)
                INNER JOIN
            products p USING (product_id)
                INNER JOIN
            product_category_name_translation pc USING (product_category_name)
        WHERE
            product_category_name_english IN ('audio' , 'auto',
                'toys',
                'cds_dvds_musicals',
                'cine_photo',
                'air_conditioning',
                'consoles_games',
                'construction_tools_construction',
                'costruction_tools_tools',
                'construction_tools_lights',
                'costruction_tools_garden',
                'construction_tools_safety',
                'cool_stuff',
                'dvds_blu_ray',
                'home_appliances',
                'home_appliances_2',
                'electronics',
                'small_appliances',
                'garden_tools',
                'industry_commerce_and_business',
                'computers_accessories',
                'musical_instruments',
                'pc_gamer',
                'computers',
                'small_appliances_home_oven_and_coffee',
                'portable_kitchen_food_processors',
                'watches_gifts',
                'security_and_services',
                'signaling_and_security',
                'tablets_printing_image',
                'telephony',
                'fixed_telephony',
                'housewares')) AS tech_price,
    ROUND(SUM(o.price) / 25) AS all_price,
    ROUND(100 * (SELECT tech_price) / ROUND(SUM(o.price) / 25)) AS tech_percent
FROM
    sellers s
        INNER JOIN
    order_items o USING (seller_id)
        INNER JOIN
    products p USING (product_id)
        INNER JOIN
    product_category_name_translation pc USING (product_category_name);
    
#3.3. In relation to the delivery time:   
#What’s the average time between the order being placed and the product being delivered?
	#We work in the orders folder
    #We define as the time interval as order_delieverd_customer_date - order_purchase_timestamp
    
    #We then calculate the time interval in hours using the query below
    #TIME_TO_SEC(TIMEDIFF(order_delivered_customer_date, order_purchase_timestamp))/3600

    
    SELECT 
		order_delivered_customer_date,
		order_purchase_timestamp,
        timediff(order_delivered_customer_date,order_purchase_timestamp),
        ROUND(TIME_TO_SEC(TIMEDIFF(order_delivered_customer_date, order_purchase_timestamp))/3600) as Δh
	FROM
		orders
	HAVING YEAR(order_delivered_customer_date) - YEAR(order_purchase_timestamp) = 0
    LIMIT 5;
	
    #We now calculate the average time interval
    SELECT 
		ROUND(AVG(TIME_TO_SEC(TIMEDIFF(order_delivered_customer_date, order_purchase_timestamp))/3600)) as avg_Δh,
        ROUND(AVG(TIME_TO_SEC(TIMEDIFF(order_delivered_customer_date, order_purchase_timestamp))/(3600*24))) as avg_Δd
	FROM
		orders;
    
	#We conclude that the average time interval is 12 days
    
    
    
#How many orders are delivered on time vs orders delivered with a delay?
    SELECT  
		count(order_id),
        CASE
			WHEN TIME_TO_SEC(timediff(order_estimated_delivery_date,order_delivered_customer_date))/3600>0 THEN 'on time'
            WHEN TIME_TO_SEC(timediff(order_estimated_delivery_date,order_delivered_customer_date))/3600<0 THEN 'late'
		END AS 'late_ontime'
	FROM
		orders
	group by late_ontime;

# There are 88649 orders delivered on time and 7827 late

#Is there any pattern for delayed orders, e.g. big products being delayed more often?

SELECT 
    oi.price, p.product_weight_g, p.product_length_cm,
    CASE
        WHEN
            TIME_TO_SEC(TIMEDIFF(order_estimated_delivery_date,
                            order_delivered_customer_date)) / 3600 > 0
        THEN
            'on time'
        WHEN
            TIME_TO_SEC(TIMEDIFF(order_estimated_delivery_date,
                            order_delivered_customer_date)) / 3600 < 0
        THEN
            'late'
    END AS 'late_ontime'
FROM
    orders AS o
        RIGHT JOIN
    order_items AS oi ON oi.order_id = o.order_id
        LEFT JOIN
    products AS p ON p.product_id = oi.product_id
order by p.product_weight_g desc;