from django.contrib import admin
from django.urls import path
from . import views
from .views import delete_segment,update_segment_texts,upload_video,merge_edited_audio_video,resend_code,chatbot_response

urlpatterns = [
	path('payment_successful', views.payment_successful, name='payment_successful'),
	path('payment_cancelled', views.payment_cancelled, name='payment_cancelled'),
	path('stripe_webhook', views.stripe_webhook, name='stripe_webhook'),
    path('', views.index, name='index'),
    path('pricing', views.pricing, name='pricing'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('verify_otp', views.verify_otp, name='verify_otp'),
    path('onboard/<int:pk>',views.onboard,name='onboard'),
    path('work_space/<int:pk>', views.work_space, name='work_space'),
    path('user_history/<int:pk>', views.user_history, name='user_history'),
    path('delete-segment/', delete_segment, name='delete_segment'),
    path('update-segment-texts/', views.update_segment_texts, name='update_segment_texts'),
    path('upload_video/<int:pk>/', upload_video, name='upload_video'),
    path('merge_edited_audio_video/<int:pk>/', merge_edited_audio_video, name='merge_edited_audio_video'),
    path('smokey/al', views.admin_login, name='admin_login'),  # Updated URL for admin login
    path('smokey/go', views.admin_side, name='admin_side'),    # Updated URL for admin side
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('delete_entry/<int:user_id>/', views.delete_entry, name='delete_entry'), 
    path('resend_code/', resend_code, name='resend_code'),
    path('save_feedback/', views.save_feedback, name='save_feedback'),
    path('profile_page/<int:pk>', views.profile, name='profile_page'),
    path('update-username/', views.update_username, name='update_username'),
    path('update_workspace/', views.update_workspace, name='update_workspace'),
    path('get_videos/<str:folder_name>/', views.get_videos, name='get_videos'),
    path('training/', views.training_page, name='training_page'),
    path('trainingVideos', views.trainingVideos, name='trainingVideos'),
    path('training_payment_successful', views.training_payment_successful, name='training_payment_successful'),
    path('training_payment_cancelled', views.training_payment_cancelled, name='training_payment_cancelled'),
    path('text_generation/<int:pk>', views.text_generation, name='text_generation'),
    path('text_to_speech/<int:pk>', views.text_to_speech, name='text_to_speech'),
    path('speech_to_text/<int:pk>/', views.speech_to_text, name='speech_to_text'),
    path('upload_audio/', views.upload_audio, name='upload_audio'),
    path('language_translation/<int:pk>', views.language_translation, name='language_translation'),
    path('text_to_image/<int:pk>', views.text_to_image, name='text_to_image'),
    path('email_us/', views.email_us, name='email_us'),
    path('chatbot_response/', chatbot_response, name='chatbot_response'),
    path('message_to_team/', views.message_to_team, name='message_to_team'),
    path('post_list/', views.post_list, name='post_list'),  # Changed from '' to 'post_list/'
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('platform/<int:pk>/', views.platform_detail, name='platform_detail'),  
    path('platform/<int:platform_id>/blog/<int:pk>/', views.platform_blog_detail, name='platform_blog_detail'),
    path('get-upload-files/<int:workspace_id>/', views.get_upload_files, name='get_upload_files'),
]

admin.site.site_header = "Clipgenie Admin"
admin.site.site_title = "Clipgenie Admin Portal"
admin.site.index_title = "Welcome to Clipgenie Portal"