from api_genderize import APIGenderize

def main():
    while True:
        name = input('Enter a name to guess the gender or type exit: ')
        if name.lower() == 'exit':
            break
        params = {'name': name}

        api = APIGenderize(params, 10)
        status, message = api.call_api()
        if status == 0:
            print(api)
            continue
        
        print('\nAn error occurred in the API call\n')
        print(message)

if __name__ == '__main__':
    main()