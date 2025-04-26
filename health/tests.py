from django.test import TestCase
from django.urls import reverse
from .models import Client, HealthProgram

class HealthSystemTests(TestCase):
    def setUp(self):
        """
        Set up initial data before each test runs:
        - Create a sample health program.
        - Create a sample client.
        - Enroll the client in the health program.
        """
        self.program = HealthProgram.objects.create(
            name='HIV Program',
            description='Health program for HIV treatment and awareness'
        )

        self.client_obj = Client.objects.create(
            first_name='Jane',
            last_name='Doe',
            date_of_birth='1992-05-12',
            gender='F',
            contact_number='9876543210'
        )
        self.client_obj.enrolled_programs.add(self.program)

    def test_program_creation(self):
        #Test that a health program is created correctly.
        self.assertEqual(HealthProgram.objects.count(), 1)
        self.assertEqual(self.program.name, 'HIV Program')

    def test_client_registration(self):
        #Test that a client is registered correctly.
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(self.client_obj.first_name, 'Jane')

    def test_client_enrollment(self):
        #Test that the client is enrolled in the health program.
        enrolled_programs = self.client_obj.enrolled_programs.all()
        self.assertIn(self.program, enrolled_programs)

    def test_client_profile_api(self):
        """
        Test the client profile API endpoint.It should return correct client details.
        It should include the enrolled programs.
        """
        url = reverse('client_profile_api', args=[self.client_obj.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = response.json()

        # Check basic client information
        self.assertEqual(data['first_name'], 'Jane')
        self.assertEqual(data['last_name'], 'Doe')
        self.assertEqual(data['gender'], 'F')

        # Check enrolled programs
        enrolled_program_names = [program['name'] for program in data['enrolled_programs']]
        self.assertIn('HIV Program', enrolled_program_names)
