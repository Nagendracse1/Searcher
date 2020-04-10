# Searcher

Create an website in python using Django framework.


The website have 3 pages:

1.App searcher
	Brief: This page will be used to get information about apps on the Apple App store or the Google Play store.

	UI: The page should be the following form
  
            A radio button/drop-down to select the store (Apple or Google Play)
            If Google Play is selected, a text input will appear which will accept the ‘Package Name’(eg. com.appxplore.voidtroopers)
            If App Store is selected, two text inputs will appear which takes app name and ‘Application ID’
            A ‘Get Info’ button to submit the form.
            App info card with the following information:
            App Icon
            App Name
            Developer Name
            Description (max 200 characters .. truncate the rest and add trailing dots(...))
            No. of Downloads
            App Rating
            No. of ratings/reviews

	Functionality: 
            Once the submit button is hit, run an AJAX request, to retrieve information about the currently submitted app.
            I used bs4 & requests website crawling libraries to retrieve the necessary information from the specified webpages. Sample page url are as follows:
            Google Play: https://play.google.com/store/apps/details?id=com.appxplore.voidtroopers
            App Store: https://apps.apple.com/in/app/void-troopers-sci-fi-tapper/id1367822033
            The entire page will not refresh, only the App Info card data will be updated with the new information.
            The submit button should stay disabled until a response is received from the server




2.Keyword finder

Brief: This page will be used to get all the keywords from the currently given url

	UI: The page should be the following form
          A text input to get the website url
          A ‘Get Keywords’ button to submit the form
          A modal/ popup to show keyword information:
          List of keywords found with related urls for each keyword
          List of recommended keywords

	Functionality: 
            Once the submit button is hit, all keywords are extracted from the given url’s meta tags (keywords, description and og:description)
            Use any website crawling libraries to retrieve the necessary information from the specified webpages.
            You may show the result of keywords on the same page or in modal / popup.
            Store all keyword information in a Model mapped to its respective url
            While retrieving keyword data, run a query on the Model and retrieve the urls on which the same keyword exists.
            If more than 3 keywords match on two urls, show the rest of the keywords from the existing url as ‘Recommended URLS’
            For eg. if url present in the model is https://www.dotabuff.com/ with keywords dota 2 stats, dota 2, statistics, dota, guides. Now if the new url entered is https://stratz.com/ which has keywords dota 2 stats, dota 2, statistics. So for stratz.com, the recommended keywords have to be dota, guides.

3.Homepage

UI: You can design the homepage as per your liking with the following constraints

            One graphic
            Buttons to both pages(App Searcher and keyword finder)
            One CSS animation
