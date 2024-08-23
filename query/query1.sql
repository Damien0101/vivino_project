--- We want to highlight 10 wines to increase our sales.
--- Which ones should we choose and why?

select name from vintages where price_euros < 50

select count(price_euros) from vintages

select count(name) from vintages
