# pylint: disable = multiple-statements
from ..contracts.extract_contract import ExtractContract


class TransformRawData:

    def transform(self, extract_contract: ExtractContract):
        transformed_information = self.__filter_and_transform_data(extract_contract)
        return transformed_information

    def __filter_and_transform_data(self, extract_contract: ExtractContract) -> list[dict]:
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_information_content
        transformed_information = []

        for data in data_content:
            transformed_data = None
            link = data['link']

            if 'artistid=' not in link: continue

            names = None
            if ', ' in data['name']: names = data['name'].split(', ')
            elif ' ' in data['name']: names = data['name'].split(' ')
            else: names = [data['name']]

            transformed_data = self.__transform_data(names, link)
            transformed_data['extraction_date'] = extraction_date
            print(transformed_data)
            transformed_information.append(transformed_data)

        return transformed_information

    def __transform_data(self, names: list, link: str) -> dict:
        link_splited = link.split('artistid=')

        if len(names) == 2:
            return {
                "first_name": names[1],
                "second_name": names[0],
                "surname": None,
                "artist_id": link_splited[1],
                "link": link
            }

        if len(names) == 3:
            return {
                "first_name": names[2],
                "second_name": names[0],
                "surname": names[1],
                "artist_id": link_splited[1],
                "link": link
            }

        return {
            "first_name": names[0],
            "second_name": None,
            "surname": None,
            "artist_id": link_splited[1],
            "link": link
        }
