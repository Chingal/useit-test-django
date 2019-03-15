from django.contrib import admin
from .models import User, Board, Idea

# Now register the new UserAdmin...
admin.site.register(User)
admin.site.register(Board)
admin.site.register(Idea)
