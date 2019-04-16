use sakila;
-- 1a. Display first & last names of all actors from the table `actor`.
SELECT first_name, last_name
FROM actor;
SELECT * FROM actor;
-- 1b. Display first & last name each actor in single column `Actor Name`.
SELECT CONCAT(first_name, ' ', last_name) AS 'Actor Name'
FROM actor;
-- 2a. Find IDnumber, firstname, lastname of an actor by firstname "Joe."
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'Joe';
-- 2b. Find all actors whose last name contain the letters `GEN`:
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE '%GEN%';
-- 2c. Find all actors lastnames contain `LI`, order rows by lastname firstname:
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name , first_name;
-- 2d. Using `IN`, display `country_id` & `country`: Afghanistan, Bangladesh, and China:
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan' , 'Bangladesh', 'China');
-- 3a. Description each actor; no queries so create a column `description` type BLOB.
ALTER TABLE actor
ADD description BLOB;
-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the `description` column.
ALTER TABLE actor
DROP COLUMN description;
-- 4a. List the last names of actors, as well as how many actors have that last name.
SELECT last_name, COUNT(last_name)
FROM actor
GROUP BY last_name;
-- 4b. List last names of actors, number of actors that last name, only for names at least two actors.
SELECT last_name, COUNT(last_name)
FROM actor
GROUP BY last_name
HAVING COUNT(last_name) >= 2;
-- 4c. The actor `HARPO WILLIAMS` was accidentally entered in the `actor` table as `GROUCHO WILLIAMS`. Write a query to fix the record.
UPDATE actor 
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO';
SELECT first_name, last_name
FROM actor
WHERE last_name = 'Williams';
-- 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. It turns out that `GROUCHO` was the correct name after all! In a single query, if the first name of the actor is currently `HARPO`, change it to `GROUCHO`.
UPDATE actor 
SET first_name = REPLACE(first_name, 'HARPO', 'GROUCHO');
SELECT first_name, last_name FROM actor WHERE last_name = 'Williams';
-- 5a. You cannot locate the schema of the `address` table. Which query would you use to re-create it?
CREATE TABLE actors (
	actor_id int(10) NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(30) NOT NULL,
    last_update DATE,
    PRIMARY KEY (last_name, actor_id)
);
-- 6a. Use `JOIN` to display the first and last names, as well as the address, of each staff member. Use the tables `staff` and `address`:
SELECT s.first_name, s.last_name, a.address 
FROM staff as s
JOIN address as a 
ON s.address_id = a.address_id;
-- select count(*) from staff;
-- 6b. Use `JOIN` to display the total amount rung up by each staff member in August of 2005. Use tables `staff` and `payment`.
SELECT SUM(amount), last_name 
FROM staff AS s
JOIN payment AS p
ON s.staff_id = p.staff_id
GROUP BY last_name;
-- 6c. List each film and the number of actors who are listed for that film. Use tables `film_actor` and `film`. Use inner join.
SELECT COUNT(actor_id), title FROM film f
INNER JOIN film_actor fa
ON f.film_id = fa.film_id
GROUP BY title;
-- 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?
SELECT f.title, COUNT(i.inventory_id) 
FROM inventory i JOIN film f
ON f.film_id = i.film_id
WHERE title = "Hunchback Impossible";

-- 6e. Using `payment`, `customer`, `JOIN`, list total paid by each customer, alphabetically by last name:
SELECT SUM(p.amount), c.last_name 
FROM payment p JOIN customer c ON c.customer_id = p.customer_id
GROUP BY c.last_name
ORDER BY c.last_name;

-- 7a. Use subqueries to display titles of movies starting w `K` & `Q` whose language is English.
SELECT title FROM film 
WHERE title LIKE 'k%' OR title LIKE 'q%' AND language_id = 'English';

/* these don't work....
WHERE title IN ('q%','k%');
WHERE title LIKE '[kq]%' AND language_id = 'English';
WHERE title LIKE '^[kq]';
WHERE title LIKE '^q';*/

-- 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.
SELECT first_name, last_name FROM actor 
WHERE actor_id IN (
	SELECT actor_id FROM film_actor 
    WHERE film_id IN (
		SELECT film_id FROM film 
		WHERE title = 'Alone Trip')
);
-- SELECT film_id FROM film WHERE title = 'Alone Trip';
-- SELECT actor_id FROM film_actor WHERE film_id = 17;
-- SELECT first_name, last_name FROM actor WHERE actor_id IN (3, 12, 13, 82, 100, 160, 167, 187);

-- 7c. Retrieve names and email addresses of all Canadian customers. Use joins.
/*SELECT cu.first_name, cu.last_name, cu.email FROM customer cu 
	JOIN address a ON cu.address_id = a.address_id
	JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
	WHERE country = 'Canada';*/
-- SELECT country_id FROM country WHERE country = 'Canada';
-- SELECT city_id FROM city WHERE country_id = 20;
-- SELECT address_id FROM address WHERE city_id = 565 OR 430 OR 383 OR 313 OR 300 OR 196 OR 179; 
-- -- Select email from customer;	 
-- SELECT store_id, address_id FROM store;
-- SELECT city_id FROM address WHERE address_id = 1 OR address_id = 2;
-- SELECT country_id FROM city WHERE city_id = 300 OR city_id = 576;
-- SELECT country FROM country WHERE country_id = 20 OR country_id = 8;
-- SELECT city_id FROM city WHERE country_id = 20;  
-- SELECT city_id FROM city WHERE country_id = 8;
-- SELECT staff_id FROM staff;
/*Only 5 customer emails (or addresses) by JOIN or subquery? 
603 rows of address_id's in 7 cities in Canada -- Actors have no addresses. 
Total 599 emails in database, but only 5 customer emails in Canada??
Only 7 cities in Canada, 1 in Australia in the database. 
AHAH! there are only 2 stores ANYwhere, 1 in Canada, 1 in Australia; only 2 staff. 
Must be the relationship between tables; try store_id index to join instead.*/
SELECT email FROM customer c
	JOIN store st ON c.store_id = st.store_id
    JOIN address a ON st.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
    WHERE country = "Canada";

-- 7d. Identify all movies categorized as _family_ films.  ((69 of them))
-- SELECT category_id FROM category
-- WHERE `name` = 'family';		-- category # 8
SELECT title, film_id FROM film
WHERE film_id IN (
	SELECT film_id FROM film_category
    WHERE category_id IN (
		SELECT category_id FROM category
		WHERE `name` = 'family')
);

-- 7e. Display the most frequently rented movies in descending order.
SELECT title, count(rental_id) as count FROM film f 
	JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON i.inventory_id = r.inventory_id
    GROUP BY title
    ORDER BY count DESC;
    
-- 7f. Display how much business ($) each store brought in. ((2 stores))
SELECT st.store_id, SUM(p.amount) as store_total 
	FROM payment p
	LEFT JOIN staff s on p.staff_id = s.staff_id
	LEFT JOIN store st ON s.staff_id = st.manager_staff_id
    GROUP BY store_id
    ORDER BY store_total DESC;

-- 7g. Write a query to display for each store its store ID, city, and country.
SELECT store_id, city, country FROM store st 
	JOIN address a ON st.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
    JOIN country co ON ci.country_id = co.country_id;

-- 7h. List top 5 genres in gross revenue, descending order. (category, film_category, inventory, payment, rental.)
SELECT SUM(amount) AS gross_revenue, `name` AS genre FROM payment p
	JOIN rental r ON p.rental_id = r.rental_id
	JOIN inventory i ON r.inventory_id = i.inventory_id
	JOIN film_category fc ON fc.film_id = i.film_id
	JOIN category c ON fc.category_id = c.category_id
    GROUP BY c.`name`
    ORDER BY gross_revenue DESC;

-- 8a. View of Top5 genres by gross revenue. 
CREATE VIEW top5genres AS 
	SELECT SUM(amount) AS gross_revenue, `name` AS genre FROM payment p
	JOIN rental r ON p.rental_id = r.rental_id
	JOIN inventory i ON r.inventory_id = i.inventory_id
	JOIN film_category fc ON fc.film_id = i.film_id
	JOIN category c ON fc.category_id = c.category_id
    GROUP BY c.`name`
    ORDER BY gross_revenue DESC;
    
-- 8b. How would you display the view that you created in 8a?
/* Hover cursor to right of VIEW name, Click on table/lightning bolt icon; 
a new code window will appear with SELECT * line and executes code.*/

-- 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.
DROP VIEW top5genres;