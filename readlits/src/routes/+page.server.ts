import { Account, ID, Client, Databases } from 'appwrite';
import type {Actions, PageServerLoad} from "./$types";

export const load: PageServerLoad = async () => {};

export const actions: Actions = {
    register: async ({ locals, request }) => {
        const body = Object.fromEntries(await request.formData());
        console.log(locals);
        console.log(body);

        const account =  new Account(locals.client)
        try {
            const newAccount = await account.create(
                ID.unique(), 
                body.email as string, 
                body.password as string, 
                body.name as string
             );
            console.log(newAccount);
        } catch(err){
            console.log(err);
        }
    },
    books: async ({ locals, request }) => {

        const databases = new Databases(locals.client);
        console.log(locals);
        try {
            const response = await databases.listDocuments(
                '6467a2917aaf8fd17198',
                'books'
            );
            console.log(response);
        } catch (error) {
            console.log(error);
        }
    },
    addbook: async ({ locals, request}) => {
        const body = Object.fromEntries(await request.formData());
        const databases = new Databases(locals.client);
        console.log(body)
        const book = {
            'name': body.name as string, 
            'description': body.description as string, 
            'rating': body.rating as number,
            'author': body.author as string
        };
        const documentId = ID.unique();
        console.log(documentId)
        console.log(book)
        try {
            const newBook = await databases.createDocument('6467a2917aaf8fd17198', '6467a33ecbefa946e984', documentId, {book});
            console.log(newBook);
        } catch (error) {
            console.log(error);
        }
    }
};
