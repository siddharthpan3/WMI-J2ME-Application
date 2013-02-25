from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from WMI.localdb.models import Sender,Data

@csrf_exempt
def insert(request):
		
	mno = request.GET.get('mno')
	temp = request.GET.get('temp')
	hum = request.GET.get('humidity')
	windvel = request.GET.get('windvelocity')

	print mno,temp,hum,windvel,"printing values"
	sender = Sender(number=int(mno))
	sender.save()

	data = Data(temperature=float(temp), humidity=float(hum), windvelocity=float(windvel), sender_id=sender.number)
	data.save()	
	
	return HttpResponse("Done")

	
