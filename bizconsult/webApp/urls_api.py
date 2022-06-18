from rest_framework import routers
from webApp import viewset


router = routers.DefaultRouter()
router.register('site-info',viewset.SiteInfoViewSet)
router.register('Social-Network',viewset.Social_NetworkViewSet)
router.register('about',viewset.AboutViewSet)
router.register('contact',viewset.ContactViewSet)
router.register('potentialite',viewset.PotentialiteViewiewSet)
router.register('banner',viewset.BannerViewSet)
#router.register('feature',viewset.FeatureViewSet)