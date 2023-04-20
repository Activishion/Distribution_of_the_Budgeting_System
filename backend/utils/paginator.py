from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class APIListPaginator(LimitOffsetPagination):
    default_limit = 1
    max_limit = 10
    
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.count,
            'results': data
        })