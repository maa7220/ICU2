from django.urls import path
from .views import (SignUpAdminView, SignUpUserView, AllUsers, PasswordResetView, VerifyOTP,
                    NurseUser, AllDoctors, AllNurses, DoctorUser, PasswordView,
                    UserDetails, LoginUser, Login, LogoutView, AddDeleteNurseUser, NursesName, CountStaffs,
                    GetUsersPatient, DoctorsName, PatientDeleteUser, GetRelatedUser,
                    SignupPatients, Patients, PatientDetailsAPI, PatientUser)

urlpatterns = [

    # ----------AUTH -------------
    path("signup_admin", SignUpAdminView.as_view(), name="signup_admin"),
    path("signup_user", SignUpUserView.as_view(), name="signup_user"),
    path("login", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("send_code", PasswordResetView.as_view(), name="send_code"),
    path("verify_otp", VerifyOTP.as_view(), name="verify_oTP"),
    path("password_confirm", PasswordView.as_view(), name="password_confirm"),

    # ---------- get users -------------
    path("get_related_user/<str:pk>",
         GetRelatedUser.as_view(), name="get_related_user"),

    path("user/profile/", LoginUser.as_view(), name="profile"),

    path("users/", AllUsers.as_view(), name="users"),
    path("users/<str:pk>", UserDetails.as_view(), name="user_detail"),

    # Return Nurse For doctor
    path("nurse/", NurseUser.as_view(), name="nurses_doctor"),
    path("nurse/<str:pk>", NurseUser.as_view(), name="nurses_doctor"),

    # Add Nurse for doctor
    path("add_nurses", AddDeleteNurseUser.as_view(), name="nurse_doctor"),
    path("delete_nurses_doctor", AddDeleteNurseUser.as_view(), name="nurse_doctor"),

    # Return Doctor For Nurse
    path("doctor/", DoctorUser.as_view(), name="doctors_nurse"),
    path("doctor/<str:pk>", DoctorUser.as_view(), name="doctor_nurse"),

    # Return All Doctors
    path("doctors/", AllDoctors.as_view(), name="doctors"),

    # Return All Nurses
    path("nurses/", AllNurses.as_view(), name="nurses"),

    # ----------------PatientAPI---------------
    path("add-patient", SignupPatients.as_view(), name="add_patient"),

    path("patients/", Patients.as_view(), name="patients"),
    path("patients/<str:pk>", PatientDetailsAPI.as_view(), name="patient-details"),

    # =================== Return Patient For one doctor or nurse (Login) =========
    path("patient_user/", PatientUser.as_view(), name="patients_user"),
    path("patient_user/<str:pk>",
         PatientUser.as_view(), name="patients_user"),


    # =================== (Admin) Return Patient For one (nurse , or doctor) ==============================================
    path("get_patients_user/<str:pk>",
         GetUsersPatient.as_view(), name="patients_user"),


    # ============================================================================
    # ============================================================================
    path("doctors_name", DoctorsName.as_view(), name="doctors_name"),
    path("nurses_name", NursesName.as_view(), name="nurses_name"),

    # ============================================================================
    path("num_staff", CountStaffs.as_view(), name="num_staff"),

    path("delete_patients_user", PatientDeleteUser.as_view(),
         name="delete_patients_user"),
]
