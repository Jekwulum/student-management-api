from rest_framework.pagination import LimitOffsetPagination


class StudentPagination(LimitOffsetPagination):
    limit_query_param = 'limit'
    offset_query_param = 'offset'
