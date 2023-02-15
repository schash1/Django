from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name="Title")
    preambule = models.CharField(max_length=1024, verbose_name="Preambule")
    body = models.TextField(blank=True, null=True, verbose_name="Body")
    body_as_markdown = models.BooleanField(default=False, verbose_name="As markdown")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ("-created",)


class CoursesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Courses(models.Model):
    objects = CoursesManager()

    name = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cost", default=0)
    cover = models.CharField(max_length=25, default="no_image.svg", verbose_name="Cover")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    def delete(self, *args):
        self.deleted = True
        self.save()


class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name="Lesson number")
    title = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ("course", "num")
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")


class CourseTeachers(models.Model):
    course = models.ManyToManyField(Courses)
    name_first = models.CharField(max_length=128, verbose_name="Name")
    name_second = models.CharField(max_length=128, verbose_name="Surname")
    day_birth = models.DateField(verbose_name="Birth date")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.name_second, self.name_first)

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

  </div>

  <!-- Footer -->

  <div class="container-lg mt-auto">
    <hr>
    <div class="row justify-content-center">
      <div class="col-sm-6 col-md-3 text-center">
        <p>
          <strong>Braniac</strong>
        </p>
        <p>
        <ul class="list-unstyled">
          <li><a href="{% url 'mainapp:main_page' %}">Домашняя</a></li>
          <li><a href="{% url 'mainapp:news' %}">Новости</a></li>
          <li><a href="{% url 'mainapp:login' %}">Войти</a></li>
        </ul>
        </p>
      </div>
      <div class="col-sm-6 col-md-3 text-center">
        <p>
          <strong>Полезное</strong>
        </p>
        <p>
        <ul class="list-unstyled">
          <li><a href="#">Положения &amp; Условия</a></li>
          <li><a href="#">Конфиденциальность &amp; Cookies</a></li>
          <li><a href="#">Документация по API</a></li>
          <li><a href="{% url 'mainapp:doc_site' %}">Документация по сайту</a>
          </li>
        </ul>
        </p>
      </div>
      <div class="col-sm-6 col-md-3 text-center">
        <p>
          <strong>Мы в социальных сетях</strong>
        </p>
        <p>
        <div class="row justify-content-around">
          <div><a href="#"><i class="fab fa-vk fa-2x"></i></a></div>
          <div><a href="#"><i class="fab fa-facebook-f fa-2x"></i></a>
          </div>
          <div><a href="#"><i class="fab fa-instagram fa-2x"></i></a>
          </div>
          <div><a href="#"><i class="fab fa-pinterest-p fa-2x"></i></a></div>
        </div>
        </p>
        <p>
          <strong>Наше приложение</strong>
        </p>
        <p>
        <div class="row justify-content-around">
          <div><a href="#"><i class="fab fa-app-store fa-2x"></i></a>
          </div>
          <div><a href="#"><i class="fab fa-google-play fa-2x"></i></a></div>
          <div><a href="#"><i class="fab fa-windows fa-2x"></i></a>
          </div>
        </div>
        </p>
      </div>
    </div>
    <div class="row justify-content-center">
      <div>
        <p><small>&copy; GeekBrains 2021</small></p>
      </div>
    </div>
  </div>

  <!-- /Footer -->




  <!-- JavaScript section -->
  <!-- Bootstrap -->
  <script src="{% static 'js/jquery-3.6.0.min.js' %}"></script>
  <script src="{% static 'js/popper.min.js' %}"></script>
  <script src="{% static 'js/bootstrap.min.js' %}"></script>

  <!-- ChartJs -->
  <script src="{% static 'js/Chart.min.js' %}"></script>

  <!-- FontAwesome -->
  <script src="{% static 'js/fontawesome.all.min.js' %}"></script>



</body>

</html>

class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name="Lesson number")
    title = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    def delete(self, *args):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ("course", "num")


class CourseTeachers(models.Model):
    course = models.ManyToManyField(Courses)
    name_first = models.CharField(max_length=128, verbose_name="Name")
    name_second = models.CharField(max_length=128, verbose_name="Surname")
    day_birth = models.DateField(verbose_name="Birth date")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.name_second, self.name_first)

    def delete(self, *args):
        self.deleted = True
        self.save()
