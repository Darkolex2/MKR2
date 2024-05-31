# recipe/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeViewsTestCase(TestCase):

    def setUp(self):
        self.recipe1 = Recipe.objects.create(title="Recipe 1", description="Description 1", date="2023-01-01")
        self.recipe2 = Recipe.objects.create(title="Recipe 2", description="Description 2", date="2023-05-15")

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/main.html')
        self.assertContains(response, self.recipe1.title)
        self.assertContains(response, self.recipe2.title)

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/recipe_detail.html')
        self.assertContains(response, self.recipe1.title)
        self.assertContains(response, self.recipe1.description)
