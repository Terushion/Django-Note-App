from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import PostItNote
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    """
    Render the home page.
    :param request: HTTP request object.
    :return: Rendered home.html template.
    """
    return render(request, "my_notes/home.html")


def view_notes(request):
    """
    View to display a list of all notes.
    :param request: HTTP request object.
    :return: Rendered template with a list of notes.
    """
    notes = (
        PostItNote.objects.all()
    )  # Grabbing all the records from the PostItNote table
    context = {
        "notes": notes,
        "page_title": "List of Notes",
    }
    return render(request, "my_notes/view_notes.html", context)


def create_note(request):
    """
    View to create a new note.
    :param request: HTTP request object.
    :return: Redirect to the view_notes page upon success.
    """
    if request.method == "POST":
        author = request.POST.get("author")
        title = request.POST.get("title")
        content = request.POST.get("content")
        PostItNote.objects.create(author=author, title=title, content=content)
        return redirect("view")
    return render(request, "my_notes/create_note.html")


def check_note(request, note_id):
    """
    View to display the details of a specific note.
    :param request: HTTP request object.
    :param note_id: ID of the note to display.
    :return: Rendered template with note details.
    """
    note = get_object_or_404(PostItNote, id=note_id)
    return render(request, "my_notes/check_note.html", {"note": note})


def edit_note(request, note_id):
    """
    View to edit an existing note.
    :param request: HTTP request object.
    :param note_id: ID of the note to edit.
    :return: Redirect to the check_note page upon success.
    """
    note = get_object_or_404(PostItNote, id=note_id)
    if request.method == "POST":
        author = request.POST.get("author")
        title = request.POST.get("title")
        content = request.POST.get("content")
        note.author = author
        note.title = title
        note.content = content
        note.save()
        return redirect("check", note_id=note.id)
    return render(request, "my_notes/edit_note.html", {"note": note})


@require_POST
def delete_note(request, note_id):
    """
    View to delete an existing note.
    :param request: HTTP request object.
    :param note_id: ID of the note to delete.
    :return: Redirect to the view_notes page upon success.
    """
    note = get_object_or_404(PostItNote, id=note_id)
    note.delete()
    return redirect("view")


def signup(request):
    """
    View to handle user signup.
    :param request: HTTP request object.
    :return: Rendered signup page with user creation form.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "my_notes/signup.html", {"form": form})


def login_view(request):
    """
    View to handle user login.
    :param request: HTTP request object.
    :return: Rendered login page with authentication form.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "my_notes/login.html", {"form": form})


@login_required
def profile(request):
    """
    View to display user profile page.
    :param request: HTTP request object.
    :return: Rendered profile page.
    """
    return render(request, "my_notes/profile.html")


@require_POST
def logout_view(request):
    """
    View to handle user logout.
    :param request: HTTP request object.
    :return: Redirect to the home page.
    """
    logout(request)
    return redirect("home")
