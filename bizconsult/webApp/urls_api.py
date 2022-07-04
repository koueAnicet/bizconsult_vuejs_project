from rest_framework import routers
from webApp import viewset
from serviceConseilApp import viewSet



router = routers.DefaultRouter()
router.register('site-info',viewset.SiteInfoViewSet)
router.register('banner',viewset.BannerViewSet)
router.register('Social-Network',viewset.SocialNetworkViewSet)
router.register('contact',viewset.ContactViewSet)
router.register('potentialite',viewset.PotentialiteViewiewSet)
router.register('about',viewset.AboutViewSet)
router.register('feature',viewset.FeatureViewSet)
#------- from service conseil------

# router = routers.DefaultRouter()
router.register('service',viewSet.ServiceViewSet)
router.register('team',viewSet.TeamViewSet)
router.register('Reseau-Social',viewSet.ReseauSocialTeamViewSet)
router.register('Testimonial',viewSet.TestimonialViewSet)