from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from books.models import Book
from comments.models import Comment
from comments.forms import CommentForm


@login_required
def add_comment(request, book_pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        form.save()
        book = Book.objects.get(pk=book_pk)

    return redirect(book.get_absolute_url())


@require_POST
@login_required
def update_comment(request):
    comment_id = request.POST.get("comment_id")
    new_text = request.POST.get("text")
    comment = Comment.objects.get(id=comment_id)

    if comment.customer == request.user.customer:
        comment.text = new_text
        comment.save()

        return JsonResponse({"success": True, "updated_text": comment.text})

    return JsonResponse({"success": False, "error": "Invalid request"})


@require_POST
@login_required
def delete_comment(request):
    comment_id = request.POST.get("comment_id")
    comment = Comment.objects.get(pk=comment_id)

    if comment.customer == request.user.customer:
        comment.delete()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False, "error": "Invalid request"})
