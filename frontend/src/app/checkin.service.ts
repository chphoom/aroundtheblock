import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError, map } from 'rxjs';

export interface User {
  pid: number;
  first_name: string;
  last_name: string;
}

export interface Checkin{
  user: User
  created_at: Date
}
export interface CheckInRequest {
  pid: number;
}

@Injectable({
  providedIn: 'root'
})
export class CheckinService {

  constructor(private http: HttpClient) {}

  /**
   * Retrieve all users registered with the check-in system.
   * 
   * @returns observable array of User objects.
   */
  getCheckins(): Observable<Checkin[]> {
    return this.http.get<Checkin[]>("/api/checkins").pipe(map(checkins=>checkins.map(checkin => {
      checkin.created_at = new Date(checkin.created_at);
      return checkin;
    })));
  }

  /**
   * Registers a user with the check-in system.
   * 
   * @param pid 9-digit UNC PID
   * @returns Obervable of User that will error if there are issues with validation or persistence.
   */
  checkIn(pid: number): Observable<Checkin> {
    let errors: string[] = [];

    if (pid.toString().length !== 9) {
      errors.push(`Invalid PID: ${pid}`);
    }

  
    if (errors.length > 0) {
      return throwError(() => { return new Error(errors.join("\n")) });
    }

    let checkinrequest: CheckInRequest = {pid};

    return this.http.post<Checkin>("/api/checkins", checkinrequest);
  }

}
