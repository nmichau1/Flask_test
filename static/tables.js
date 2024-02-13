import { db } from '@vercel/postgres';
 
const client = await db.connect();
await client.sql`CREATE TABLE Pets ( Name varchar(255), Owner varchar(255) );`;
   