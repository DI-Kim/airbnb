from rest_framework.test import APITestCase
from . import models


class TestAmenities(APITestCase):
    NAME = "Amenity Test"
    DESC = "Amenity Desc"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )

        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME)
        self.assertEqual(data[0]["description"], self.DESC)

    def test_create_amenity(self):
        new_amenity_name = "New Amenity"
        new_amenity_description = "New Amenity Desc."

        #! test case 1
        response = self.client.post(
            self.URL,
            data={"name": new_amenity_name, "description": new_amenity_description},
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(data["name"], new_amenity_name)
        self.assertEqual(data["description"], new_amenity_description)

        #! test case 2
        response = self.client.post(
            self.URL,
            data={"name": "old_amenity", "description": new_amenity_description},
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertIsNot(data["name"], new_amenity_name)
        self.assertEqual(data["description"], new_amenity_description)

        #! test case 3
        response = self.client.post(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            400,
            "Not 400 status code",
        )
        self.assertIn("name", data)


class TestAmenity(APITestCase):
    NAME = "Test Amenity"
    DESC = "Test Desc"
    URL = "/api/v1/rooms/amenities/1"
    WRONG_URL = "/api/v1/rooms/amenities/12"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get(self.WRONG_URL)

        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], self.NAME)
        self.assertEqual(data["description"], self.DESC)

    def test_put_amenity(self):
        # code challenge
        # serializer가 유효해서 유저가 업데이트 할 수 있는 경우
        # 유효하지 않을 경우
        pass

    def test_delete_amenity(self):
        response = self.client.delete(self.URL)

        self.assertEqual(response.status_code, 204)
