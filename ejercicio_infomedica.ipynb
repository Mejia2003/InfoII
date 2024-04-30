import pydicom

class DicomFile:
    def __init__(self, filename):
        self.dataset = pydicom.dcmread(filename)

    def get_patient_name(self):
        return self.dataset.PatientName

    def get_study_description(self):
        return self.dataset.StudyDescription

    def view_image_in_axial_plane(self):
        import matplotlib.pyplot as plt

        plt.imshow(self.dataset.pixel_array, cmap="gray")
        plt.title("Imagen axial")
        plt.show()

    def view_image_in_sagittal_plane(self):
        import matplotlib.pyplot as plt

        plt.imshow(self.dataset.pixel_array.T, cmap="gray")
        plt.title("Imagen sagital")
        plt.show()

    def view_image_in_coronal_plane(self):
        import matplotlib.pyplot as plt

        plt.imshow(self.dataset.pixel_array[:, :, ::-1], cmap="gray")
        plt.title("Imagen coronal")
        plt.show()

    def get_image_size(self):
        return (self.dataset.Rows, self.dataset.Columns)

    def get_number_of_slices(self):
        return self.dataset.NumberOfSlices


# Example usage
filename = "dicom_image.dcm"

dicom_file = DicomFile(filename)

patient_name = dicom_file.get_patient_name()
study_description = dicom_file.get_study_description()

print("Nombre del paciente:", patient_name)
print("Descripción del estudio:", study_description)

dicom_file.view_image_in_axial_plane()
dicom_file.view_image_in_sagittal_plane()
dicom_file.view_image_in_coronal_plane()

image_size = dicom_file.get_image_size()
number_of_slices = dicom_file.get_number_of_slices()

print("Tamaño de la imagen:", image_size)
print("Número de cortes:", number_of_slices)