import json
from django.shortcuts import render

# Create your views here.
# In shutdown_app/views.py
import subprocess
from django.http import HttpResponse, JsonResponse

def shutdown(request):
    # Execute the shutdown command
    subprocess.call(["shutdown", "/s", "/t", "0"])
    return HttpResponse("Shutting down...")

def set_volume(request, volume):
    volume = 65535 * (int(volume) / 100)
    subprocess.call(['C:\\o\\nircmdc.exe', 'setsysvolume', str(volume)]) #
    return HttpResponse(f"Volume set to {volume}%")

def lockscreen(request):
    cmd='rundll32.exe user32.dll, LockWorkStation'
    subprocess.call(cmd)
    return HttpResponse("Locking Screen")

import pyautogui

def move_mouse(request, x, y):
    x = int(x)
    y = int(y)
    
    pyautogui.moveTo(x, y)
    
    return HttpResponse("Moved the mouse")

def left_click_mouse(request):
    pyautogui.leftClick()
    return JsonResponse({'message': 'Coordinates received successfully'})

def right_click_mouse(request):
    pyautogui.rightClick()
    return JsonResponse({'message': 'Coordinates received successfully'})

def coordinates_view(request):
    return render(request, 'coordinates.html')

def send_coordinates(request):
    if request.method == 'POST':
        try:
            post_data = json.loads(request.body.decode("utf-8"))

            x_corr = post_data.get('x')
            y_corr = post_data.get('y')

            move_mouse(request, x_corr, y_corr)
            return JsonResponse({'message': 'Coordinates received successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
    