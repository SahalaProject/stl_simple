from rest_framework import pagination


class MyCursorPagination(pagination.CursorPagination):
    """
    Cursor 光标分页 性能高，安全
    """
    page_size = 10
    ordering = '-update_time'
    page_size_query_param = "size"
    page_query_param = 'page'
    max_page_size = 20


class MyPageNumberPagination(pagination.PageNumberPagination):
    """
    普通分页，数据量越大性能越差
    """
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 20


class PageNumberPagination_Testcases(pagination.PageNumberPagination):
    """
    普通分页，数据量越大性能越差
    """
    page_size = 12
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 12

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        # response = super(PageNumberPagination_Testcases,self).get_paginated_response(data)
        page_size = self.get_page_size(request)
        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        self.page = paginator.page(page_number)



        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)


class PageNumberPagination_TaskTestcases(PageNumberPagination_Testcases):
    """
    普通分页，数据量越大性能越差
    """
    page_size = 5000
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 5000

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        # response = super(PageNumberPagination_Testcases,self).get_paginated_response(data)
        page_size = self.get_page_size(request)
        paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages

        self.page = paginator.page(page_number)

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)