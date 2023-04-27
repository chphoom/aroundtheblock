import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError, map, catchError, tap, of, from, ReplaySubject } from 'rxjs';
import { User } from './models';
export { User } from './models';
import { Router } from '@angular/router';
import { JwtHelperService } from '@auth0/angular-jwt';


const REPLAY_LAST = 1;

/**
 * This class handles the registration concerns of the system including the ability
 * to create new registrations and retrieve a list of registered users.
 */
@Injectable({
  providedIn: 'root'
})
export class RegistrationService {

  private isAuthenticated: ReplaySubject<boolean> = new ReplaySubject(REPLAY_LAST);
  public isAuthenticated$: Observable<boolean> = this.isAuthenticated.asObservable();

  constructor(private jwt: JwtHelperService, private http: HttpClient, private router: Router) {
    this.authenticate();
  }

  private authenticate() {
    let token: string | Promise<string> | null = localStorage.getItem('authToken');
    if (token === null) {
      this.isAuthenticated.next(false);
    } else {
      let observable: Observable<string>;
      if (typeof token === 'string') {
        observable = of(token);
      } else {
        observable = from(token);
      }
      observable.subscribe((token) => {
        if (this.jwt.isTokenExpired(token)) {
          localStorage.removeItem('authToken');
          localStorage.removeItem('bearerToken');
          this.isAuthenticated.next(false);
        } else {
          this.isAuthenticated.next(true);
        }
      })
    }
  }

  // Set if user is logged in or not
  /* public setAuthenticated(value: boolean): void {
    this.isAuthenticatedSubject.next(value);
  }

  public getAuthenticated(): Observable<boolean> {
    return this.isAuthenticatedSubject.asObservable()
  } */

  /**
   * Retrieve all users registered with the check-in system.
   * 
   * @returns observable array of User objects.
   */
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>("/api/registrations").pipe(map(users=>users.map(user => {
      user.created = new Date(user.created);
      return user;
    })));
  }

  getUser(email: string): Observable<User> {
    return this.http.get<User>(`/api/users/${email}`)
  }

  getUserN(name: string): Observable<User> {
    return this.http.get<User>(`/api/username/${name}`)
  }

  updateUser(email: string, pronouns: string | null, displayName: string | null, priv: boolean | null, pfp: string | null, bio: string | null, connectedAccounts: string[] | null) {
    let query = "";
    if (pronouns) {
        query += `pronouns=${pronouns}&`;
    }
    if (displayName) {
        query += `displayName=${displayName}&`;
    }
    if (priv != null) {
        query += `private=${priv}&`;
    }
    if (pfp) {
        query += `pfp=${pfp}&`;
    }
    if (bio) {
        query += `bio=${bio}&`;
    }
    if (connectedAccounts?.length) {
        query += `connectedAccounts=${connectedAccounts.join(",")}&`;
    }
    if (query) {
        query = "?" + query.slice(0, -1); // remove the trailing "&" or "?" if query is not empty
    }
    return this.http.put<User>(`api/users/${email}${query}`, connectedAccounts)
  }

  saveChallenge(email: string, challenge_id: number) {
    return this.http.put<User>(`/api/savec?email=${email}&challenge_id=${challenge_id}`,{})
  }

  unsaveChallenge(email: string, challenge_id: number) {
    return this.http.put<User>(`/api/unsavec?email=${email}&challenge_id=${challenge_id}`,{})
  }

  savePost(email: string, post_id: number) {
    return this.http.put<User>(`/api/savep?email=${email}&post_id=${post_id}`,{})
  }

  unsavePost(email: string, post_id: number) {
    return this.http.put<User>(`/api/unsavep?email=${email}&post_id=${post_id}`,{})
  }

  /**
   * Registers a user into database.
   * 
   * @param email 
   * @param displayName username
   * @param password
   * @param created
   * @returns Obervable of User that will error if there are issues with validation or persistence.
   */
  registerUser(email: string, displayName: string, password: string, confirm: string): Observable<User> {
    let errors: string[] = [];

    //TODO: email  validation
    if (email === "") {
      errors.push(`Email required.`);
    }

    if (displayName === "") {
      errors.push(`Username required.`);
    }

    if (password === "") {
      errors.push(`Password required.`)
    }
    
    if (password !== confirm) {
      errors.push('Please confirm that your passwords match')
    }

    if (errors.length > 0) {
      return throwError(() => { return new Error(errors.join("\n")) });
    }

    let user: User = {email, displayName, password, created: new Date(), private: false, bio: "", pronouns: "", pfp: "https://i.imgur.com/1MwzVBB.png", userPosts: [], savedChallenges: [], savedPosts: [], connectedAccounts: []};

    return this.http.post<User>("api/registrations",user);
  }

  /**
   * Logs User in and returns resulting JWT Token
   * 
   * @param email 
   * @param password
   * @returns Obervable of Token that will error if there are issues with validation or persistence.
   */
  loginUser(email: string, password: string){
    const body = new URLSearchParams();
    body.set('username', email);
    body.set('password', password);
    //this.setAuthenticated(true);

    return this.http.post<any>('/api/login', body.toString(), {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    }).pipe(
      tap(res => {
        localStorage.setItem('authToken', res.token);
        this.isAuthenticated.next(true);
      }),
      catchError(error => {
        console.error(error);
        return throwError(() => error);
      })
    );
  }

  /**
   * Retrieves whether User is logged in based on presence of valid JWT token in local storage
   * @returns boolean value
   */
  isLoggedIn(): Observable<boolean> {
    const token = localStorage.getItem('authToken');
    return of(token !== null);
  }

  /**
   * log out
   */
  logout(): void {
      localStorage.removeItem("authToken");
      localStorage.removeItem("bearerToken");
      this.isAuthenticated.next(false);
  }
  
  /**
   * Retrieves User thats logged in
   * @returns User
   */
  getUserInfo(): Observable<User> {
    const token = localStorage.getItem('authToken');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    });
    return this.http.get<User>(`/api/login`, { headers })
  }
}
