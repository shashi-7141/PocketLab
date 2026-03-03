from django.shortcuts import render, redirect, get_object_or_404
from .models import ExperimentLog


def log_list(request):
    logs = ExperimentLog.objects.all()
    context = {
        'logs': logs,
        'page_title': 'Experiment Logs'
    }
    return render(request, 'logs/list.html', context)


def log_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        details = request.POST.get('details')
        observations = request.POST.get('observations')
        results = request.POST.get('results')

        ExperimentLog.objects.create(
            title=title,
            date=date,
            details=details,
            observations=observations,
            results=results
        )

        return redirect('logs:list')

    return render(request, 'logs/form.html')


def log_detail(request, pk):
    log = get_object_or_404(ExperimentLog, pk=pk)
    return render(request, 'logs/detail.html', {'log': log})


def log_update(request, pk):
    log = get_object_or_404(ExperimentLog, pk=pk)

    if request.method == 'POST':
        log.title = request.POST.get('title')
        log.date = request.POST.get('date')
        log.details = request.POST.get('details')
        log.observations = request.POST.get('observations')
        log.results = request.POST.get('results')

        log.save()
        return redirect('logs:detail', pk=log.pk)

    context = {
        'log': log
    }

    return render(request, 'logs/form.html', context)


def log_delete(request, pk):
    log = get_object_or_404(ExperimentLog, pk=pk)

    if request.method == 'POST':
        log.delete()
        return redirect('logs:list')

    return render(request, 'logs/delete.html', {'log': log})