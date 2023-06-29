from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class disContactSerializer(serializers.ModelSerializer):

	personalname = CharField(source="title", required=True)
	#message = CharField(source="description", required=False)
	personalemail = EmailField(required=True)
	#contactno=CharField(source="title", required=True)
	#changes
	companyname = CharField( required=True)
	companyemail = EmailField(required=True)
	companyurl= CharField(required=True)
	companycity= CharField(required=True)
	companystate= CharField(required=True)
	companyzipcode= CharField(required=True)
	companyaddress= CharField(source="description",required=True)
	#experience
	designation=CharField(required=True)
	industry=CharField(required=True)
	years=CharField(required=True)
	question=CharField(required=True)
	speciality=CharField(required=True)

	class Meta:
		model = models.disContact
		fields = (
			'personalname',
			'personalemail',
			'companyname',
			'companyemail',
			'companyurl',
			'companycity',
			'companystate',
			'companyzipcode',
			'companyaddress',
			'designation',
			'industry',
			'years',
			'question',
			'speciality',
		)