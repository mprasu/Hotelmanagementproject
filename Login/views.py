from django.shortcuts import render
from django.views.generic import View
from Login.forms import LoginForm
# Create your views here.
from Signup.models import SignupModel
class LoginView(View):
	form_class = LoginForm
	template_name = 'login.html'
	def get(self, request, *args, **kwargs):
		form = self.form_class()#initial=self.initial
		return render(request, 'login.html', {'form': form})
	def post(self,request):
		uname=request.POST['username']
		mailid=request.POST['email']
		recs=SignupModel.objects.filter(Name=uname,Email_id=mailid)
		if(recs.count()==0):
			return render(request, 'login.html',{"msg":"invalid username/password"})
		else:
			return render(request,'inbox.html')