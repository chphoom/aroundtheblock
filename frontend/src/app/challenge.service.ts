import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { Challenge } from './models';

@Injectable({
  providedIn: 'root'
})
export class ChallengeService {

  constructor(private http: HttpClient) { 

    /**
     * Retrieve all Challenges in the system.
     * 
     * @returns an observable array of Challenge objects.
     */
    getAllChallenges(): Observable<Challenge[]> {
      return this.http.get<Challenge[]>("/api/challenges");
    }

  }
}
