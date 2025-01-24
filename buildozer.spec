[app]

# عنوان التطبيق
title = تطبيق Kivy

# اسم الحزمة (يجب أن يكون فريدًا)
package.name = myapp

# اسم النشاط الرئيسي
package.domain = org.test

# إصدار التطبيق
version = 1.0.0

# الملف الرئيسي للتطبيق
source.dir = .

# الملف الرئيسي للتطبيق
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*,fonts/*

# المتطلبات
requirements = kivy

# إعدادات Android
android.api = 30
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.arch = armeabi-v7a