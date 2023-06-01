# World of Shows Beta Version

## Table of Contents
- [World of Shows Beta Version](#world-of-shows-beta-version)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Base App](#base-app)
    - [Scope of the Homepage](#scope-of-the-homepage)
      - [Find Shows:](#find-shows)
      - [Post Show:](#post-show)
      - [Take Classes:](#take-classes)
      - [Share Class:](#share-class)
      - [Find Venues:](#find-venues)
      - [Rent out Venue:](#rent-out-venue)
      - [Find Auditions:](#find-auditions)
      - [Share Audition:](#share-audition)
      - [Find Playreads:](#find-playreads)
      - [Share Playread:](#share-playread)
    - [Scope of the Sign-Up Functionality](#scope-of-the-sign-up-functionality)
    - [Scope of the User Dashboard](#scope-of-the-user-dashboard)
      - [**My Tickets**](#my-tickets)
        - [Sold](#sold)
        - [Bought](#bought)
      - [**My Venues**](#my-venues)
        - [Booked](#booked)
        - [Rented Out](#rented-out)
      - [**My Classes**](#my-classes)
        - [Enrolled](#enrolled)
        - [Posted](#posted)
      - [**My Auditions**](#my-auditions)
        - [Registered](#registered)
        - [Participated](#participated)
        - [Posted](#posted-1)
      - [**My Playreads**](#my-playreads)
        - [Registered](#registered-1)
        - [Posted](#posted-2)
      - [**Profile**](#profile)
        - [1. **Profile Type Selection:**](#1-profile-type-selection)
        - [2. **Shared Profile Sections:**](#2-shared-profile-sections)
        - [3. **Theater Group-Specific Sections:**](#3-theater-group-specific-sections)
        - [4. **Direct Message/Chat:**](#4-direct-messagechat)
    - [Scope of Global search](#scope-of-global-search)
  - [Shows App](#shows-app)
    - [Show Listings](#show-listings)
    - [Show Detail Page](#show-detail-page)
    - [Interactive Cast and Crew](#interactive-cast-and-crew)
    - [Ticketing Functionality (Will not be available in the Beta version)](#ticketing-functionality-will-not-be-available-in-the-beta-version)
    - [Saved Shows](#saved-shows)
    - [Show Management](#show-management)
    - [Integration with Venues App](#integration-with-venues-app)
  - [Auditions App](#auditions-app)
    - [Audition Listings](#audition-listings)
    - [Audition Detail Page](#audition-detail-page)
    - [Interactive Roles and Role Details](#interactive-roles-and-role-details)
    - [Audition Submission](#audition-submission)
    - [Saved Auditions](#saved-auditions)
    - [Audition Management](#audition-management)
    - [Integration with User Profiles](#integration-with-user-profiles)
  - [Classes App](#classes-app)
    - [Class Listings](#class-listings)
    - [Class Detail Page](#class-detail-page)
    - [Enrollment and Registration](#enrollment-and-registration)
    - [Saved Classes](#saved-classes)
    - [Class Management](#class-management)
    - [Integration with User Profiles](#integration-with-user-profiles-1)
  - [Playreads App](#playreads-app)
    - [Playread Listings](#playread-listings)
    - [Playread Detail Page](#playread-detail-page)
    - [Participation and RSVP](#participation-and-rsvp)
    - [Saved Playreads](#saved-playreads)
    - [Playread Management](#playread-management)
    - [Integration with User Profiles](#integration-with-user-profiles-2)
  - [Venues App](#venues-app)
    - [Venue Listings](#venue-listings)
    - [Venue Detail Page](#venue-detail-page)
    - [Interactive Availability Calendar](#interactive-availability-calendar)
    - [Booking and Reservation](#booking-and-reservation)
    - [Saved Venues](#saved-venues)
    - [Venue Management](#venue-management)
    - [Integration with Shows, Auditions, Playreads, and Classes Apps](#integration-with-shows-auditions-playreads-and-classes-apps)
    - [Integration with User Profiles](#integration-with-user-profiles-3)
  - [Deployment to Production environment](#deployment-to-production-environment)


## Overview
World of Shows is broken down into 6 Django apps:
- Base
- Shows
- Venues
- Classes
- Auditions
- Play Reads

## Base App

This app handles all global functionality.
- Homepage
- Sign-up functionality.
- User Dashboard.
- Global search.

### Scope of the Homepage

The Homepage in the Base app provides users with easy access to various features and functionalities through interactive cards. Each card represents a specific action or category related to the theater community. The following are the cards available on the Homepage:

#### Find Shows:
- Description: Discover upcoming shows in the theater community.
- Action: Clicking the card directs users to the Shows app (Shows front page), where they can browse and search for shows based on different criteria, such as title, genre, location, or date.
- Images: Show-related image representing a production or performance.

#### Post Show:
- Description: Share information about your upcoming show or production.
- Action: Clicking the card leads users to the Shows app (Post show page), where they can create show listings and add details for their productions.
- Images: Image representing a theater performance or production.

#### Take Classes:
- Description: Explore classes and workshops for theater enthusiasts.
- Action: Clicking the card directs users to the Classes app (Classes front page), where they can browse available classes and workshops.
- Images: Image representing a class or workshop environment.

#### Share Class:
- Description: Share details about your upcoming class or workshop.
- Action: Clicking the card leads users to the Classes app (Post class page), where they can create class listings and provide information about the class or workshop.
- Images: Image representing a class or workshop environment.

#### Find Venues:
- Description: Discover venues available for hosting performances or events.
- Action: Clicking the card directs users to the Venues app (Venues front page), where they can explore venue listings, view details, and contact venue owners or managers.
- Images: Image showcasing a theater or performance venue.

#### Rent out Venue:
- Description: Rent out your venue.
- Action: Clicking the card directs users to the Venues app (Rent venue page).
- Images: Image representing a venue available for rental.

#### Find Auditions:
- Description: Find open castings and auditions near you.
- Action: Clicking the card redirects users to the Auditions app (Auditions front page), where they can view audition listings, roles, requirements, and submit their applications.
- Images: Image representing the audition process or performers.

#### Share Audition:
- Description: Post auditions to find the best talent for your production.
- Action: Clicking the card leads users to the Auditions app (Share auditions page), where they can create and manage audition listings, specify roles, and set audition requirements.
- Images: Image depicting an audition setting or casting process.

#### Find Playreads:
- Description: Discover and explore playreads shared by the theater community.
- Action: Clicking the card leads users to the Playreads app (Playreads front page), where they can browse and search for playreads.
- Images: Image representing a play or script.

#### Share Playread:
- Description: Share your playread with the community.
- Action: Clicking the card leads users to the Playreads app (Share playread page)
- Images: Image representing a play or script.


### Scope of the Sign-Up Functionality

For the Beta version, user signup will be via email. 

1. Design and implement a user registration page where new users can sign up using their email addresses.
2. Create a form to capture user registration details, including email address and password.
3. Implement backend logic to handle user registration:
   - Validate user input and ensure the email address is unique.
   - Hash and securely store the user's password.
   - Create a new user account in the database.
   - Generate a verification token or link for email verification.
   - Send a verification email to the user's provided email address.
4. Design and implement an email verification page where users can verify their email addresses by clicking on the verification link.
5. Implement backend logic to handle email verification:
   - Verify the user's email address based on the verification token or link.
   - Update the user's account status to "verified" upon successful verification.
6. Consider implementing additional features like password strength validation and email address format validation.

### Scope of the User Dashboard

The User Dashboard should include the following sections:
- My Tickets
- My Venues
- My Classes
- My Playreads
- Saved items
- Profile 
- Direct Message (part of the user profile) 

#### **My Tickets**
- Display a list of tickets related to the user's activities in the theater community.
- Include two subsections: "Sold" and "Bought."

##### Sold
- List the tickets sold by the user for their own shows or events.
- Include details such as the event title, date, time, venue, ticket status eg sold out, and the number of tickets sold.
- If there are no tickets sold, display a message saying "You have not sold tickets to any shows."

##### Bought
- Display a list of tickets purchased by the user for shows or events organized by others.
- Include details such as the event title, date, time, venue, ticket status, and any additional information.
- If there are no tickets bought, display a message saying "You have not bought tickets to any shows."

  
#### **My Venues**
- Display a list of venues related to the user's activities in the theater community.
- Include two subsections: "Booked" and "Rented Out."

##### Booked
- List the venues the user has reserved for their own events or performances.
- Include details such as the venue name, location, reservation period, and any additional information.
- Provide options to manage bookings, make changes, or cancel reservations.
- If there are no booked venues, display a message saying "You have not booked any venues."

##### Rented Out
- Display a list of venues the user has posted for rent.
- Include details such as the venue name, location, rental period, and any additional information.
- Provide options to manage rental listings, make changes, or remove listings.
- If there are no rented out venues, display a message saying "You have not rented out any venues."

#### **My Classes**
- Display a list of classes or workshops related to the user's activities in the theater community.
- Include two subsections: "Enrolled" and "Posted."

##### Enrolled
- List the classes or workshops the user has enrolled in.
- Include details such as the class title, instructor, date, time, location, and any additional information.
- Provide options to access course materials, join virtual sessions, or communicate with the instructor.
- If there are no enrolled classes, display a message saying "You have not enrolled in any classes."

##### Posted
- Display a list of classes or workshops posted by the user.
- Include details such as the class title, instructor, date, time, location, and any additional information.
- Provide options to manage class listings, make changes, or remove listings.
- If there are no posted classes, display a message saying "You have not posted any classes."

#### **My Auditions**
- Display a list of auditions related to the user's activities in the theater community.
- Include three subsections: "Registered," "Participated," and "Posted."

##### Registered
- List the upcoming auditions the user has registered for.
- Include details such as the audition title, date, time, location, and any additional information.
- Provide options to manage registration, view audition details, or cancel registration.
- If there are no registered auditions, display a message saying "You have not registered for any auditions."

##### Participated
- List the auditions the user has participated in.
- Include details such as the audition title, date, time, location, and any additional information.
- Provide options to view audition results, communicate with casting directors, or take further action.
- If there are no participated auditions, display a message saying "You have not participated in any auditions."

##### Posted
- List the auditions the user has posted.
- Include details such as the audition title, date, time, location, and any additional information.
- Provide options to manage the posted audition, edit details, or remove the posting.
- If there are no posted auditions, display a message saying "You have not posted any auditions."

#### **My Playreads**
- Display a list of playreads related to the user's activities in the theater community.
- Include two subsections: "Registered" and "Posted."

##### Registered
- List the playreads the user has registered for or plans to attend.
- Include details such as the playread title, date, time, location, and any additional information.
- Provide options to view playread details, manage registration, or cancel attendance.
- If there are no registered playreads, display a message saying "You have not registered for any playreads."

##### Posted
- List the playreads the user has posted or organized.
- Include details such as the playread title, date, time, location, and any additional information.
- Provide options to manage the posted playread, edit details, or remove the posting.
- If there are no posted playreads, display a message saying "You have not posted any playreads."



#### **Profile**

##### 1. **Profile Type Selection:**

   - Provide an option during the profile creation process for users to select their profile type, such as "Individual" or "Theater Group."
   - Based on the selected profile type, customize the profile page layout and fields accordingly.

##### 2. **Shared Profile Sections:**

   *Profile Picture:*

   - Allow users to upload a profile picture or avatar to represent their identity on the platform.
   - Provide options for users to crop or resize their profile picture for optimal display.

   *Contact Details:*

   - Include fields for users to provide their contact information, such as email address and phone number.
   - Optionally, provide additional fields for users to enter their preferred method of contact or communication.

   *Social Media Links:*

   - Offer fields where users can enter their social media links to platforms like TikTok, Instagram, YouTube, Twitter, or other relevant platforms.


   *Bio/About:*
   - Allow users to provide a brief description of themselves.
   
   *Productions:*
   - Display a list of productions or shows performed by the theater group or individual.
   - Each listing should include details such as production title, brief description, genres, theater group or hosts, and date of production.
   - For individuals, include the role(s) they played in each production as tags or labels.
   - Clicking on a listing will lead to a detailed view with additional information like cast, crew, and other production details.

   *Open Classes, Auditions, Play reads, Venues*
   - These sections will be displayed only if the user has posted any listings.

##### 3. **Theater Group-Specific Sections:**  
   *Members:*
   - Display a list of members who are part of the theater group.
   - The names of the members should be clickable and lead to their profile page.

   *Events:*
   - List upcoming and past events organized by the theater group.
   - For upcoming events, include details such as event title, date, time, location, and registration information.
   - Provide a brief description of each event and any special highlights or activities.
   - For past events, showcase the event title, date, location, and a summary of the event's success or key takeaways.

##### 4. **Direct Message/Chat: Will not be part of the Beta release**

   - Enable a direct messaging or chat feature for users to communicate with each other.
   - Provide options for users to manage their conversations, such as archiving, deleting, or marking as unread.

### Scope of Global search
To implement the global search functionality across the specific apps in World of Shows (Base, Shows, Venues, Classes, Auditions, Play Reads), you can follow these steps:

1. Design the Search Bar Component: Create a reusable search bar component that can be included on every page of your platform. This component should have an input field where users can enter their search queries and a search button or icon to trigger the search.

2. Implement Search Functions in Each App: In each app, define a search function in the respective view that handles the search functionality specific to that app. For example:

   - In the Shows app, create a `search_shows` function in the show views that searches for shows based on the show titles, descriptions, genres, or other relevant attributes.
   - In the Venues app, create a `search_venues` function in the venue views that searches for venues based on the venue names, locations, capacities, or other relevant attributes.
   - In the Classes app, create a `search_classes` function in the class views that searches for classes based on the class titles, instructors, locations, or other relevant attributes.
   - In the Auditions app, create a `search_auditions` function in the audition views that searches for auditions based on the audition titles, dates, locations, or other relevant attributes.
   - In the Play Reads app, create a `search_playreads` function in the play read views that searches for play reads based on the play read titles, dates, locations, or other relevant attributes.

   Implement the search functions in their respective views, considering the specific data and logic of each app. These functions will handle searching, displaying results, and handling empty results within their respective views.

3. Import Search Functions: In the global search component, import the search functions from the corresponding views where they are defined. You can import the necessary modules or files that contain the search functions for each app.

4. Execute Search Functions: When a user enters a search query and triggers the search, determine the current app or module context. Based on the context, invoke the corresponding search function from the imported views. For example:

   - If the user is on a page related to shows, invoke the `search_shows` function from the show views with the search query.
   - If the user is on a page related to venues, invoke the `search_venues` function from the venue views with the search query.
   - Similarly, invoke the relevant search functions for classes, auditions, and play reads based on the user's context.

   The invoked search function will handle searching, displaying results, and handling empty results within its respective app.




## Shows App

The Shows app is responsible for managing show listings in the theater community. It provides the following features and functionality:

### Show Listings
- Display a list of shows with relevant details, including title, description,  host, genres, and a poster image for visual representation.
- Allow users to browse, filter and search for shows based on different criteria, such as title, genre, location, price or date.
- Implement pagination or infinite scrolling for efficient navigation through a large number of show listings.

### Show Detail Page
- Provide a dedicated page for each show, showcasing comprehensive information about the production.
- Include sections for show description,  cast and crew details, venue information, showtimes, ticketing information, and any additional relevant information.
- Display a poster image for the show to visually represent the production.

### Interactive Cast and Crew
- Enhance user engagement by allowing users to explore the profiles of cast members and production crew involved in the show.


### Ticketing Functionality (Will not be available in the Beta version)
- Allow users to purchase tickets to shows directly through the app.
- Implement a secure and user-friendly ticket booking process.
- Provide options for selecting seating preferences, ticket quantities, and payment methods.
- Generate electronic tickets with unique identifiers and deliver them to users via email or in-app access.

### Saved Shows
- Enable users to save shows for later reference and easy access.
- Implement a save functionality, such as a bookmark or favorite icon, for users to add shows to their saved items list.
- Provide a dedicated section in the User Dashboard to display saved shows.
- Allow users to remove saved shows if they are no longer of interest.

### Show Management
- Allow show organizers to create, edit, and manage their show listings.
- Implement an intuitive interface for show creation, enabling organizers to input relevant details, upload images or media, and add a poster image for the show.
- Provide options for updating show information, such as modifying showtimes, adding or removing cast members, or updating ticket prices.


### Integration with Venues App
- Collaborate with the Venues app to associate shows with specific venues.
- Implement seamless integration to display venue information within show listings and detail pages.
- Allow users to navigate to the venue details directly from the show page.

## Auditions App

The Auditions app is designed to streamline the audition process in the theater community. It provides the following features and functionality:

### Audition Listings
- Display a list of auditions with relevant details, including title, description, date, location, and roles available.
- Allow users to browse, filter, and search for auditions based on different criteria, such as title, date, location, or role type.
- Implement pagination or infinite scrolling for efficient navigation through a large number of audition listings.

### Audition Detail Page
- Provide a dedicated page for each audition, showcasing comprehensive information about the casting call.
- Include sections for audition description, role details, audition requirements, submission instructions, and any additional relevant information.

### Interactive Roles and Role Details
- Allow users to view details about each role, such as character descriptions, requirements, and any specific instructions.
- Enable users to express interest in specific roles and indicate their intention to audition.

### Audition Submission
- Allow users to apply for auditions using their World of Shows profile, simplifying the application process.
- Implement a secure and user-friendly process for users to submit their audition materials.
- Provide options for uploading headshots, resumes, demo reels, or any other required materials.
- Allow users to specify their preferred audition date and time, if applicable.
- Provide confirmation of successful submission and relevant notifications or updates.

### Saved Auditions
- Enable users to save auditions for later reference and easy access.
- Implement a save functionality, such as a bookmark or favorite icon, for users to add auditions to their saved items list.
- Provide a dedicated section in the User Dashboard to display saved auditions.
- Allow users to remove saved auditions if they are no longer of interest.

### Audition Management
- Allow casting directors or audition organizers to create, edit, and manage audition listings.
- Implement an intuitive interface for audition creation, enabling organizers to input relevant details, specify roles, and set audition requirements.
- Provide options for updating audition information, extending submission deadlines, or modifying role details.
- Allow audition organizers to view a list of all the applicants who have submitted for a particular audition.
- Implement clickable links to navigate to the user profiles, showcasing their background, experience, and contact information.
- The user profiles will have chat or direct message functionality allowing audition organizers and applicants to communicate effectively regarding audition details, results, and feedback. The chat functionality will be implemented in the Base app.


### Integration with User Profiles
- Enable users to view the profiles of casting directors or audition organizers associated with each audition.


## Classes App

The Classes app is designed to provide a platform for organizing and managing theater classes and workshops. It offers the following features and functionality:

### Class Listings
- Display a list of theater classes and workshops with relevant details, including title, description, instructor, date, time, location, and class type.
- Allow users to browse, filter, and search for classes based on different criteria, such as title, instructor, date, location, or class type.
- Implement pagination or infinite scrolling for efficient navigation through a large number of class listings.

### Class Detail Page
- Provide a dedicated page for each class, showcasing comprehensive information about the class or workshop.
- Include sections for class description, instructor bio, class objectives, schedule, requirements, and any additional relevant information.

### Enrollment and Registration
- Allow users to enroll in classes and workshops of their choice.
- Implement a registration process that collects necessary information from users, such as name, contact details, and payment details if applicable.
- Provide confirmation of successful enrollment and relevant notifications or updates.

### Saved Classes
- Enable users to save classes for later reference and easy access.
- Implement a save functionality, such as a bookmark or favorite icon, for users to add classes to their saved items list.
- Provide a dedicated section in the User Dashboard to display saved classes.
- Allow users to remove saved classes if they are no longer of interest.

### Class Management
- Allow class organizers or instructors to create, edit, and manage class listings.
- Implement an intuitive interface for class creation, enabling organizers to input relevant details, specify class objectives, schedule, requirements, and set class capacity.
- Provide options for updating class information, extending registration deadlines, or modifying class details.
- Allow class organizers to view a list of enrolled students for each class.
- Enable communication between class organizers and enrolled students through chat or direct message functionality within user profiles.

### Integration with User Profiles
- Enable users to view the profiles of class instructors or organizers associated with each class.
- Implement clickable links to navigate to the user profiles, showcasing their background, expertise, and contact information.
- Allow users to communicate with class instructors or organizers through chat or direct message functionality within user profiles.

The Classes app aims to provide a centralized platform for theater enthusiasts to discover, enroll, and manage their theater class or workshop experiences, while facilitating effective communication and engagement between class organizers and students within the theater community.


## Playreads App

The Playreads app is designed to facilitate the organization and participation in play reading sessions within the theater community. It offers the following features and functionality:

### Playread Listings
- Display a list of upcoming play reading sessions with relevant details, including title, date, time, location, and play description.
- Allow users to browse, filter, and search for playreads based on different criteria, such as title, date, location, or genre.
- Implement pagination or infinite scrolling for efficient navigation through a large number of playread listings.

### Playread Detail Page
- Provide a dedicated page for each play reading session, showcasing comprehensive information about the selected play.
- Include sections for play description, playwright information, character list, and any additional relevant information.

### Participation and RSVP
- Allow users to express their interest in participating in play reading sessions.
- Implement an RSVP process that collects necessary information from users, such as name, contact details, and preferred role (if applicable).
- Provide confirmation of successful RSVP and relevant notifications or updates.

### Saved Playreads
- Enable users to save playreads for later reference and easy access.
- Implement a save functionality, such as a bookmark or favorite icon, for users to add playreads to their saved items list.
- Provide a dedicated section in the User Dashboard to display saved playreads.
- Allow users to remove saved playreads if they are no longer of interest.

### Playread Management
- Allow playread organizers to create, edit, and manage play reading sessions.
- Implement an intuitive interface for playread creation, enabling organizers to input relevant details, specify play information, date, time, and location.
- Provide options for updating playread information, extending RSVP deadlines, or modifying session details.
- Allow playread organizers to view a list of participants for each session.
- Enable communication between playread organizers and participants through chat or direct message functionality within user profiles.

### Integration with User Profiles
- Enable users to view the profiles of playread organizers or facilitators associated with each session.
- Implement clickable links to navigate to the user profiles, showcasing their background, experience, and contact information.
- Allow users to communicate with playread organizers or facilitators through chat or direct message functionality within user profiles.


## Venues App

The Venues app serves as a comprehensive platform for managing and exploring theater venues within the theater community. It offers the following features and functionality:

### Venue Listings
- Display a list of theater venues with relevant details, including name, location, seating capacity, facilities, and a description of the venue.
- Allow users to browse, filter, and search for venues based on different criteria, such as location, seating capacity, amenities, or availability.
- Implement pagination or infinite scrolling for efficient navigation through a large number of venue listings.

### Venue Detail Page
- Provide a dedicated page for each theater venue, showcasing comprehensive information about the location.
- Include sections for venue description, available facilities, seating arrangements, rental rates, and any additional relevant information.
- Display images or virtual tours of the venue to give users a visual representation of the space.

### Interactive Availability Calendar
- Allow venue owners or managers to update the availability of their venues through an intuitive calendar interface.
- Enable users to view the availability of each venue, helping them make informed decisions for scheduling events or productions.

### Booking and Reservation
- Enable users to inquire about venue availability and make reservations for specific dates and times.
- Implement a secure and user-friendly booking process, including options for specifying event details, desired amenities, and contact information.
- Provide confirmation of successful bookings, along with relevant notifications or updates.

### Saved Venues
- Enable users to save venues for later reference and easy access.
- Implement a save functionality, such as a bookmark or favorite icon, for users to add venues to their saved items list.
- Provide a dedicated section in the User Dashboard to display saved venues.
- Allow users to remove saved venues if they are no longer of interest.

### Venue Management
- Allow venue owners or managers to create, edit, and manage venue listings.
- Implement an intuitive interface for venue creation, enabling owners to input relevant details, upload images or virtual tours, and specify amenities and rental rates.
- Provide options for updating venue information, modifying availability, or adjusting pricing.

### Integration with Shows, Auditions, Playreads, and Classes Apps
- Collaborate with the Shows, Auditions, Playreads, and Classes apps to associate specific shows, auditions, playreads, and classes with relevant venues.
- Implement seamless integration to display venue information within show, audition, playread, and class listings and detail pages. Eg. By implementing a get_venue_details view function within venues app that will be imported in the other apps allowing users to navigate to the venue details directly from the show, audition, playread, or class pages.
- Enable venue owners or managers to specify the availability of their venues for shows, auditions, playreads, and classes.
- Provide options for organizers to select a venue when creating or managing shows, auditions, playreads, or classes.



### Integration with User Profiles
- Enable users to view the profiles of venue owners or managers associated with each venue.
- Allow users to communicate with venue owners or managers through chat or direct message functionality within user profiles.




## Deployment to Production environment
