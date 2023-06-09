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
    book: async ({ locals, request }) => {
      const bookId = request.params.id;
      const databases = new Databases(locals.client);
      const book = await databases.getDocument('books', bookId);
      console.log(book);
      return {
        props: { book }
      };
    },
    addbook: async ({ locals, request}) => {
        const body = Object.fromEntries(await request.formData());
        const databases = locals.database;
        const book = {
            'name': body.name as string, 
            'description': body.description as string, 
            'rating': body.rating as number,
            'Author': body.author as string
        };
        const documentId = ID.unique();
        console.log(book)
        try {
            const newBook = await databases.createDocument(locals.database_id, locals.book_collection, documentId, book);
            console.log(newBook);
        } catch (error) {
            console.log(error);
        }
    },
    login: async ({ locals, request, cookies }) => {
        const body = Object.fromEntries(await request.formData());
        console.log(locals);
        console.log(body);
        let authUser;
        const account =  new Account(locals.client)
        try {
            const session = await account.createEmailSession(body.email as string, body.password as string);
            console.log(session);
            const currDate = new Date();
            const sessionExp = new Date(session.expire);
            const diff = sessionExp.getTime() - currDate.getTime() / 1000;

            cookies.set("appwrite-session", session.$id, {
                path: "/",
                httpOnly: true,
                expires: new Date(sessionExp),
            });
            
            
        } catch(err){
            console.log(err);

        }
        console.log(authUser);
    }




};
