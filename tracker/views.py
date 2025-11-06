from django.shortcuts import render, get_object_or_404, redirect
from .models import HealthRecord
from .forms import HealthRecordForm

# Просмотр всех записей
def record_list(request):
    records = HealthRecord.objects.all()
    return render(request, 'tracker/record_list.html', {'records': records})

# Создание новой записи
def record_create(request):
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = HealthRecordForm()
    return render(request, 'tracker/record_form.html', {'form': form, 'title': 'Добавить запись'})

# Редактирование
def record_edit(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk)
    if request.method == 'POST':
        form = HealthRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')
    else:
        form = HealthRecordForm(instance=record)
    return render(request, 'tracker/record_form.html', {'form': form, 'title': 'Редактировать запись'})

# Удаление
def record_delete(request, pk):
    record = get_object_or_404(HealthRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'tracker/record_confirm_delete.html', {'record': record})

