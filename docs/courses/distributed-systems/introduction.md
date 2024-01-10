---
layout: default
title: Introduction
parent: Distributed-Systems
grand_parent: Courses
---

# Introduction
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

# Introduction

## 분산 시스템이란 무엇인가?

- 분산 시스템은 사용자에게 단일 일관된 시스템으로 나타나는 자율 컴퓨팅 요소의 모음
- “A collection of autonomous computing elements (nodes), which appears to its users as a single coherent system”

### 분산시스템의 두가지 특징

- 독립적인 컴퓨팅 요소
- 사용자에게 단일시스템 처럼 보여야 한다.

특징 1 : Collection of Autonomous Nodes 자율 컴퓨팅 요소의 집합

- Independent Behavior 독립적인 행동 - 시간개념으로 자율적 → 동기화, 조정문제 발생
- 노드 컬렉션으로 그룹 관리 - 열린그룹 / 폐쇄 그룹
- 조직 - 오버레이 네트워크로 구성됨

1. Structured Overlay 구조화 된 오버레이

<img src="introduction/Untitled.png" width="500"/>

2. Unstructured Overlay 구조화 되지 않은 오버레이

<img src="introduction/Untitled 1.png" width="500"/>

특징 2 : Single Coherent System 단일 코히어런트 시스템

- 분산시스템은 하나의 일관된 시스템으로 나타나야 한다는 의미
- 즉 노드의 집합 전체는 사용자와 시스템간의 상호작용이 어디서, 언제, 어떻게 발생하는지에 관계없이 동일하게 작동하여야 함
  Keyword : Distribution transparency (유동투명성)

## 분산시스템의 목표

- 리소스를 사용 가능하게 만들기
- 유통 투명성
- 개방상태
- 확장성

### Middleware : the OS of Distributed Systems

- Distributed system organized in a middleware layer

<img src="introduction/Untitled 2.png" width="500"/>

### 분산 시스템의 속성

- Heterogeneity 이기종성
- Explicit communications 명시적 통신
- Isolation 격리
- Concurrency 동시성
- Extensibility 확장성
- Mobility 이동성
- Partial Failure 부분실패
- Multiple Authorities 여러권한

## 분산 시스템의 과제

- Heterogeneity 이기종성 지원
  네트워크, 하드웨어, 운영체제, 프로그래밍 언어 의 이기종성을 지원하여야 함
  → Middleware 미들웨어와 Mobile Code 모바일 코드를 이용
  미들웨어 : 분산 메커니즘에 덜 관심을 둔 분산 앱에 공통 레이어를 제공함
  모바일 코드 : 한 컴퓨터에서 다른 컴퓨터로 전송되어도 실행할 수 있는 코드(JVM-자바 가상머신) 이 있는 자바 코드
- Openness 개방성
  시스템의 확장성(extensibility) 또는 재구성(reconfigurability)을 결정하는 기준
  기본 환경의 이질성에 관계없이 다른 구성 요소의 서비스와 상호 작용 허용
  → Key factor : 일관성 (Coherence)
  개방형 분산 시스템의 목표 :
  - Interperability 상호 운용성 : 다른 두가지 시스템이 공존하고 함께 작동할 수 있음
  - Composability 조합성 : 단일 분산 시스템을 위해 컴포넌트가 개발될수도 있지만 컴포넌트 들이 re-use되는 경우가 많다.
  - Extensibility 확장성 : 원래의 구성요소에 영향을 주지않고 새 구성요소를 추가하거나 기존 구성요소를 교체할 수 있다.
- Scalability 확장성
  사용자 및 리소스를 추가하여도 눈에 띄는 성능저하나 관리 복잡성이 증가하지 않아야 함
  확장성을 위한 고려사항 :
  - 물리적 자원 비용 (Cost of phyiscsal resources)
  - 성능 손실 (Performance loss)
  - 소프트웨어 리소스 부족 (Software resource shortage)
  - 성능 병목 현상 (Performance bottleneck)
    Scalability Components:
  - Size scalability 크기 확장성 - 성능이나 리소스 부족을 해결하기 위해 확장 (사용자 및 프로세스 수)
  - Geographic scalability 지리적 확장성 - 사용자와 어플리케이션이 멀리 떨어져 생기는 통신 지연을 줄이기 위해 (노드 간 최대거리)
  - Administrative scalability 관리 확장성 - 많은 독립된 관리 조직에 걸쳐 있는 경우에도 시스템을 관리하기 위해 (관리 도메인 수)
    Scaling techniques 스케일링 기술
  - Hiding communication latencies
  - Partitioning data and computations across multiple machines
  - Replication and caching
    스케일링 기술 : 분포(분할) , 복제/캐싱
- Partial Failure 부분 실패

  Partial Failure : A system is considered faulty once its behavior is no longer consistent with its specification

  장애 처리 기술 :

  - Fault detection 오류감지
  - Fault masking 문제 마스킹
  - Fault tolerance 문제 허용
  - Recovery from failures 장애 복구
  - Redundancy 중복성

- Concurrency 동시성

  Concurrent access to a shared resource may cause inconsistency of the resource

  공유 리소스에 대한 동시 엑세스로 인해 리소스 불일치가 발생할 수도 있음

  - 업데이트가 손실, 일관되지 않은 검색이 초래할 수 있음.

  해결 방안 : 트랜잭션의 작업을 직렬화(한번에 하나씩) 해야 한다.

  To avoid possible problems due to concurrent access,
  operations of related transactions must be serialized (one-at-a-time)

- Security 보안

  - Authentication 입증(누가)
  - Authorization 권한부여(무엇을)
  - Encryption and Decryption 암호화 및 암호 해독

- Distribution Transparency 배포 투명성
  분리에서 파생된 속성을 은폐하여 분산시스템을 단일 통합 시스템처럼 보이게 하는 추상화 개념/매커니즘
  유동 투명성의 유형 :
  - Access 접근
  - Location 위치
  - Relocation 재배치
  - Migration 이동
  - Replication복제
  - Concurrency 동시성
  - Failure 실패

## 분산 시스템의 유형

- High Performance Distributed Computing
  - 많은 분산 시스템이 고성능 컴퓨팅을 위해 구성됨.
    예시)
    Parallel Computing 병렬 컴퓨팅
    Cluster Computing 클러스터 컴퓨팅
    Grid Computing 그리드 컴퓨팅
    Cloud Computing 클라우드 컴퓨팅
- Distributed Information Systems
  - Transaction processing system
    트랜잭션 : ACID(원자성, 일관성, 격리, 지속성)을 충족하는 개체의 상태에 대한 작업 모음입니다
- Distributed Systems for Pervasive Computing
  - 노드가 작고 이동성이 있으며 종종 더 큰 시스템에 내장되는 차세대 분산 시스템. 시스템이 사용자 환경에 자연스럽게 혼합된다는 사실을 특징으로 함.
  - 세가지 하위 유형 :
    - Ubiquitous system 유비쿼터스 시스템
    - Mobile computing 모바일 컴퓨팅
    - senser network 센서 네트워크
