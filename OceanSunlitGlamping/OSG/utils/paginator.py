"""
自定義的分頁組件，使用前須做以下程序
在view函數中:
    def XXX_list(request):
        # 1. 根據自己的情況篩選資料
        queryset = models.Admin.objects.all()

        # 2.new出分頁物件
        page_obj = Paginator(request, queryset)

        context = {
            'queryset': page_obj.page_queryset,  # 分完頁的資料
            'page_string': page_obj.html()       # 頁碼
        }
        return render(request, 'admin_list.html', context)

在HTML頁面中:
    {% for obj in queryset %}
        {{ obj.xx }}
    {% endfor %}

    <nav aria-label="Page navigation">
      <ul class="pagination">
          {{ page_string }}
      </ul>
    </nav>

"""
import copy
from django.utils.safestring import mark_safe


class Paginator(object):
    def __init__(self, request, queryset, page_param='page', page_size=10, plus=5):
        """
        :param request: 請求的對象
        :param queryset: 符合分頁條件的資料
        :param page_size: 每頁顯示多少筆資料
        :param page_param: 在URL中傳遞的參數(取得分頁頁碼)
        :param plus: 顯示前後N頁
        """
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, '1')
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * self.page_size
        self.end = page * self.page_size
        self.page_queryset = queryset[self.start:self.end]

        # 總頁數
        total_count = queryset.count()
        total_page_count, remainder = divmod(total_count, self.page_size)
        if remainder:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 計算出前後5頁

        if self.total_page_count <= 2 * self.plus + 1:
            # 當資料少於11頁時
            start_page = 1
            end_page = self.total_page_count
        else:
            # 當資料超過11頁時
            if self.page <= self.plus:
                # 當前頁數<5時
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.total_page_count:
                    #  當前頁數+5 >總頁數
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    #  當前頁數 > 5
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 首頁
        self.query_dict.setlist(self.page_param, [1])
        page_start_list = ['<li class="page-item"><a class="page-link" href="?{}">首頁</a></li>'.format(self.query_dict.urlencode())]

        # 上一頁
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
        else:
            self.query_dict.setlist(self.page_param, [1])
        prevP = ('<li class="page-item"><a class="page-link" href="?{}" aria-label="Previous"><span '
                 'aria-hidden="true">&laquo;</span></a></li>').format(self.query_dict.urlencode())
        page_start_list.append(prevP)

        # 頁碼
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                currentP = '<li class="page-item active"><a class="page-link" href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                currentP = '<li class="page-item"><a class="page-link" href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_start_list.append(currentP)

        # 下一頁
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
        nextP = ('<li class="page-item"><a class="page-link" href="?{}" aria-label="Next"><span '
                 'aria-hidden="true">&raquo;</span></a></li>').format(self.query_dict.urlencode())
        page_start_list.append(nextP)

        # 最後頁
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_start_list.append('<li class="page-item"><a class="page-link" href="?{}">最後頁</a></li>'.format(self.query_dict.urlencode()))

        return mark_safe(''.join(page_start_list))

