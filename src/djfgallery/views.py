import json
import flickrapi

from django.views.generic import TemplateView


class AlbumListView(TemplateView):
    template_name = "gallery/album_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        api_key = u'6cf69c2dd5bcc4034f999f7d53e498cc'
        api_secret = u'd8c0b93b0a1305b4'

        flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
        # photos = flickr.photos.search(user_id='73509078@N00', per_page='10')
        sets = flickr.photosets.getList(user_id='76341745@N00')
        context['album_list'] = json.loads(sets.decode('utf-8'))
        return context