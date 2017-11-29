from rest_framework.metadata import BaseMetadata

#This file is created for custom browser preflight options
#This makes OPTIONS request faster as its shorter
#By Mikael Ahonen
class MinimalMetadata(BaseMetadata):
	"""
	Don't include field and other information for `OPTIONS` requests.
	Just return the name and description.
	"""
	def determine_metadata(self, request, view):
		return {
			#'name': view.get_view_name(),
			#'description': view.get_view_description(),
			'name':'none',
		}