'use client';

import { Post } from '@/types/post';
import { useEffect, useState } from 'react';

const Page = () => {
  const [posts, setPosts] = useState<Post[]>([]);

  const getPosts = async () => {
    try {
      const response = await fetch(`/api/posts`);
      const result = await response.json();
      setPosts(result.posts as Post[]);
    } catch (error: any) {
      console.error(error.message);
    }
  };

  useEffect(() => {
    getPosts();
  }, []);

  return (
    <>
      <h1>This client components</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.content}</p>
          </li>
        ))}
      </ul>
    </>
  );
};

export default Page;
