from django.urls import reverse
from django.shortcuts import render
from django.views.generic import CreateView,View
from Signup.models import SignupModel
from django.http import HttpResponseRedirect

class SignupView(View):
	def get(self,request):
		return render(request,'signup.html')	
	def post(self,request):
		uname=request.POST['username']# a1 is the name given for fileds in signup.html page
		age=request.POST.get('age')
		mailid=request.POST.get('mailid')
		pwd=request.POST.get('password')
		confpwd=request.POST.get('confirmpassword')
		phone=request.POST.get('phone')
		location=request.POST.get('location')
		state=request.POST.get('state')
		country=request.POST.get('country')
		address=request.POST.get('address')
		myfile=request.FILES['myfile']
		recs=SignupModel.objects.all()
		emailexist="This mail is already registered"
		e=0
		for rec in recs:
			if rec.Email_id==mailid:
				e=1
				break
		if e==1:
			return render(request,'signup.html',{'emailexist':emailexist})
		else:	
		 	f=SignupModel(Name=uname,Age=age,Email_id=mailid,Password=pwd,ConfirmPassword=confpwd,Phonenumber=phone,Location=location,State=state,Country=country,Address=address,Image=myfile,)
		 	f.save()
		 	success_message="Your registration is success Now you can login"
		 	return render(request,'success.html',{"success_message":success_message})

		
"""class SignupView(CreateView):
    model =SignupModel 
    template_name = 'signup.html'
    fields='__all__'
    def post(self,request):
      uname=request.POST['username']# a1 is the name given for fileds in signup.html page
      age=request.POST.get('age')
      mailid=request.POST.get('mailid')
      pwd=request.POST.get('password')
      confpwd=request.POST.get('confirmpassword')
      phone=request.POST.get('phone')
      location=request.POST.get('location')
      state=request.POST.get('state')
      country=request.POST.get('country')
      address=request.POST.get('address')
      myfile=request.FILES['myfile']
      recs=SignupModel.objects.all()#signup is my model name
      emailexist="This mail is already registered"
      e=0
      for rec in recs:
         if rec.Email_id==mailid:
            e=e+1
            break
      if e>=1:
         return render(request,'signup.html',{'emailexist':emailexist})
      else:
         f=SignupModel(Name=uname,Age=age,Email_id=mailid,Password=pwd,ConfirmPassword=confpwd,Phonenumber=phone,Location=location,State=state,Country=country,Address=address,Image=myfile,)
         f.save()
         success_message="Your registration is success Now you can login"
         return render(request,'signup.html',{"success_message_key":success_message})

#    def get_success_url(self):
 #       return reverse('login')

  def form_valid(self, form):
        print("form_valid")
        model = form.save(commit=False)
        #print(model.Name)
	#save returns model object with out commit node ,so helps us to add some fields which are not there in model.
        #model.submitted_by = self.request.user
        model.save()
        return HttpResponseRedirect(self.get_success_url())
"""
