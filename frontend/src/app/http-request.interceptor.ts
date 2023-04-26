import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpResponse,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators'
import { LoadingService } from './loading.service';
import { RegistrationService } from './registration.service';

@Injectable({
    providedIn: 'root'
})
export class HttpRequestInterceptor implements HttpInterceptor {

  constructor(
    private loading: LoadingService, private authService: RegistrationService
  ) {}

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (request.method === "GET") {
      this.loading.setLoading(true);
    } else {
      this.loading.setSending(true);
    }

    return next.handle(request)
      .pipe(
        catchError((e) => {
            if (request.method === "GET") {
              this.loading.setLoading(false);
            } else {
              this.loading.setSending(false);
            }
            if (e instanceof HttpErrorResponse) {
              if (e.status === 401) {
                this.authService.logout();
              } else {
                this.loading.error(e);
              }
              throw e;
            }
            return of(e);
        }),
        tap((e) => {
            if (e instanceof HttpResponse) {
              if (request.method === "GET") {
                this.loading.setLoading(false);
              } else {
                this.loading.setSending(false);
              }
            }
        })
      );
  }
}