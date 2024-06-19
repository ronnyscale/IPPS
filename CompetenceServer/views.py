from django.shortcuts import render, get_object_or_404
from core.models import ParentDiscipline, Competency, Discipline


def home_view(request):
    return render(request, "competence_server/home.html")


def disciplines(request):
    parent_disciplines = ParentDiscipline.objects.prefetch_related("disciplines").all()
    return render(
        request,
        "competence_server/disciplines.html",
        {"parent_disciplines": parent_disciplines},
    )


def competencies(request):
    competencies = Competency.objects.all()
    return render(
        request, "competence_server/competencies.html", {"competencies": competencies}
    )


def discipline_detail_view(request, slug):
    discipline = get_object_or_404(Discipline, slug=slug)
    competencies = discipline.competencies.all()
    # competencies = Competency.objects.filter(disciplinecompetency__discipline=discipline)
    return render(
        request,
        "competence_server/discipline_detail.html",
        {"discipline": discipline, "competencies": competencies},
    )


def competency_detail_view(request, slug):
    competency = get_object_or_404(Competency, slug=slug)
    disciplines = competency.disciplines.all()
    return render(
        request,
        "competence_server/competency_detail.html",
        {"competency": competency, "disciplines": disciplines},
    )


def search_view(request):
    query = request.GET.get("q")
    if query:
        disciplines = Discipline.objects.filter(
            name__icontains=query
        ) | Discipline.objects.filter(code__icontains=query)
        competencies = Competency.objects.filter(
            name__icontains=query
        ) | Competency.objects.filter(code__icontains=query)
    else:
        disciplines = Discipline.objects.none()
        competencies = Competency.objects.none()

    return render(
        request,
        "competence_server/search_results.html",
        {"disciplines": disciplines, "competencies": competencies},
    )
