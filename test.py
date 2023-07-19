from DicomRTTool import DicomReaderWriter
import numpy as np
import os
import SimpleITK as sitk

Dicom_reader = DicomReaderWriter(get_images_mask=False)
# path = 'C:\users\brianmanderson\Patients\'
path = '/data1/organ_for_lung_cancer/LCTSC-Train-S1-001'

Dicom_reader.down_folder(path)
# See all rois in the folders
for roi in Dicom_reader.all_rois:
    print(roi)

# Contour_Names = ['heart']
Contour_Names = ['Liver']
associations = {'Liver_BMA_Program4': 'Liver', 'Liver': 'Liver'}
# path = 'C:\users\brianmanderson\Patients\Patient_1\CT_1\'
path = '/data1/organ_for_lung_cancer/LCTSC-Train-S1-001/11-16-2003-RTRCCTTHORAX8FLow Adult-39664/0.000000-CTRespCT-cran  3.0  B30s  50 Ex-63530'
# Dicom_reader = DicomReaderWriter(get_images_mask=True, Contour_Names=Contour_Names)
Dicom_reader = DicomReaderWriter(get_images_mask=True, Contour_Names=Contour_Names, associations=associations)

Dicom_reader.Make_Contour_From_directory(path)
image = Dicom_reader.ArrayDicom
mask = Dicom_reader.mask
# mask_1 = mask[:,:,:,0]
# mask_2 = mask[:,:,:,1]
#
# final_mask_1 = sitk.GetImageFromArray(mask_1)
# final_mask_2 = sitk.GetImageFromArray(mask_2)
#
# sitk.WriteImage(final_mask_1,
#                         '/data1/organ_for_lung_cancer/out/' + 'mask_1' + '.nii.gz')
# sitk.WriteImage(final_mask_2,
#                         '/data1/organ_for_lung_cancer/out/' + 'mask_2' + '.nii.gz')




pred = np.zeros(
    [mask.shape[0], mask.shape[1], mask.shape[2], 2])  # prediction needs to be [# images, rows, cols, # classes]
pred[:, 200:300, 200:300, 1] = 1
#
output_path = "/data1/organ_for_lung_cancer/out"
Dicom_reader.with_annotations(mask ,output_path,ROI_Names=['written_liver'])
# Dicom_reader.with_annotations(pred, output_path, ROI_Names=['test'])
# Dicom_reader.with_annotations(mask, output_path, ROI_Names=['written_liver'])

'''
Write the images and annotations as niftii files in parallel!
'''

# Dicom_reader.write_parallel(out_path=output_path,excel_file=os.path.join('.','MRN_Path_To_Iteration.xlsx'))
