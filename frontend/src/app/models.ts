export interface User {    
    email: string, 
    displayName: string, 
    password: string, 
    created: Date,
    private: boolean,
    bio: string,
    pronouns: string, 
    pfp: string, 
    userPosts: Post[] | undefined,
    savedChallenges: Challenge[] | undefined,
    savedPosts: Post[] | undefined,
    connectedAccounts: string[] | undefined
}

export interface Challenge { 
    id: number | undefined,
    posts: Post[],
    noun: string, 
    verb: string, 
    adj: string, 
    emotion: string, 
    style: string, 
    colors: string[],
    // type: string,
    start: Date | null,
    end: Date | null,
    createdBy: string | null
}

export interface Post {    
    id: number | undefined,
    img: string, 
    title: string,
    desc: string, 
    private: boolean,
    created: Date,
    challenge: number,
    user_id: string,
    comments: Comment[],
    tags: string[]
}

export interface Comment {
    id: number | undefined,
    commenter: User | string,
    user_id: string,
    post: number,
    replies: Comment[],
    text: string,
    created: Date
}

export interface TokenResponse {
    access_token: string;
    token_type: string;
  }
  