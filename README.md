# social_network
# Django REST application Social Network

- User model with usernamefield = email, and model Post which is always associated with the user.
- Each user can create Posts, as well as delete only their own Posts.
- Each user can Like and Dislike each Post, only 1 time, as well as remove their Like or Dislike.
- An endpoint with user activity has been implemented, where you can see the last login of the user and the time of the last active action.
- Implemented Registration for users, as well as endpoint Profile with information about the user.
- Implemented token authentication (JWT token)


__API end-points:__
- token/
- token/refresh/
- swagger/
- api/posts/
- api/posts/id
- api/posts/id/like
- api/posts/id/dislike
- api/signup/
- api/profile/
- api/analytics/
- api/user-activity/username


__Used tools:__    
:heavy_check_mark: Python     
:heavy_check_mark: Django REST Framework    
:heavy_check_mark: JWT authentication [Simple JWT]      
:heavy_check_mark: Swagger  
:heavy_check_mark: SQLite database    
