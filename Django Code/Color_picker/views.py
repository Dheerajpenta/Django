
from rest_framework.views import APIView
from rest_framework.response import Response
import sys

from urllib.request import urlopen
import io
from colorthief import ColorThief
import webcolors

class srcList(APIView):
    def get(self, request):
        image_src = request.GET['src']
        image_src = image_src.replace(" ", "%20")
        fd = urlopen(image_src)
        f = io.BytesIO(fd.read())
        color_thief = ColorThief(f)
        rgb = color_thief.get_color(quality=1)
        value = webcolors.rgb_to_hex(rgb)
        return Response({'logo_border': value ,'dominant_color': value })
