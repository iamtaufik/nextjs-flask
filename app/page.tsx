'use server';

import { Post } from '@/types/post';

const getPosts = async (): Promise<Post[]> => {
  try {
    const response = await fetch(`${process.env.BASE_URL}/api/posts`);
    const result = await response.json();
    return result.posts as Post[];
  } catch (error: any) {
    console.error(error.message);
    return [];
  }
};

export default async function Home() {
  const posts = await getPosts();
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </li>
      ))}
    </ul>
  );
}
