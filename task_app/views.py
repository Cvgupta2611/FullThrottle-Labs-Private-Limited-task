from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def view_data(request):
    response = dict()
    data_list = list()
    if request.method == 'GET':
        user_data = UserTable.objects.all().values_list()
        for i in user_data:
            data = {'id':i[0],
                    'real_name':i[1],
                    'tz':i[2]}
            id = i[0]
            activity = Activity.objects.filter(user_id=id).values_list()
            activity_list = list()
            for j in activity:
                activity_data = {'start_date':j[1],
                                 'end_date':j[2]}
                activity_list.append(activity_data)
            data.update({'activity_periods':activity_list})
            data_list.append(data)
        print(data_list)
        response.update({'ok':'true'})
        response.update({'member':data_list})
        print()
        return JsonResponse(response)