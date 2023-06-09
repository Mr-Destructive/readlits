import type { Handle } from "@sveltejs/kit";
import { Account, Client, Databases } from "appwrite";

export const handle: Handle = async ({ event, resolve }) => {
    const client = new Client()
        .setEndpoint('http://127.0.0.1:8001/v1')
        .setProject('6467a226111048c72b2c');
    event.locals.client = client
    event.locals.database = new Databases(client);
    event.locals.database_id = '6467a2917aaf8fd17198';
    event.locals.book_collection = '6467a33ecbefa946e984';
    event.locals.review_collection = '6472219e144e1f6135ea';
    event.locals.question_collection = '647221aa3a027f39c40a';
    event.locals.answer_collection = '647221b240e735f5bf1a';
    event.locals.quiz_collection = '647221b914446462e25d';
    event.locals.quiz_result_collection= '647222075e1b0254b10e';
    event.locals.bookling_collection = '64722a605a4fd6bd4858';

    const account = new Account(client);
    try{
        event.locals.account = await account.get();
    } catch(err){
    }
    return resolve(event);
};
