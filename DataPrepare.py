import xml.etree.ElementTree as ET

def extract_data_from_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()

    image_paths = []
    image_sizes = []
    image_labels = []
    bounding_boxes = []

    for image in root:
        bbs_of_image = []
        labels_of_image = []

        for bbs in image.findall('taggedRectangles'):
            for bb in bbs:
                if not bb[0].text.isalnum():
                    continue
                if 'é' in bb[0].text.lower() or 'ñ' in bb[0].text.lower():
                    continue
                
                bbs_of_image.append(
                    [
                        float(bb.attrib['x']),
                        float(bb.attrib['y']),
                        float(bb.attrib['width']),
                        float(bb.attrib['height']),
                    ]
                )
                labels_of_image.append(bb[0].text.lower())

        #store
        image_paths.append(image[0].text)
        image_sizes.append((int(image[1].attrib['x']), int(image[1].attrib['y'])))
        bounding_boxes.append(bbs_of_image)
        image_labels.append(labels_of_image)
    
    return image_paths, image_sizes, image_labels, bounding_boxes

image_paths, image_sizes, image_labels, bounding_boxes = extract_data_from_xml('SceneTrialTrain/words.xml')

