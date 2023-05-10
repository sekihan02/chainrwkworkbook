# Dapr（Distributed Application Runtime）について

Daprは独立した機能同士を集めたマイクロサービスアプリケーションを簡易化するために設計されたオープンソースのアプリ実行中に動作するシステム環境であるランタイムです。

## 特徴

1. ポータブル: KubernetesやDockerなど任意のホスト環境で実行でき、どのプラットフォーム上でも同じコードを実行でき、プラットフォーム固有の制約や依存関係に大きく左右されず、多くの環境で実行できる。![overview-kubernetes.png](https://docs.dapr.io/images/overview-kubernetes.png)
2. 拡張性: プラグインアーキテクチャを採用していて独自の機能を追加したり、既存の機能をカスタマイズしたりできるようになっています。![overview-kubernetes.png](https://docs.dapr.io/images/overview-kubernetes.png)
3. 言語とフレームワークに依存しない: gRPCまたはHTTP APIを介してアプリケーションと通信し、多くの言語と互換性があり複数言語に対して互換性があります。![buildframework](https://thinkit.co.jp/sites/default/files/article_node/1764209.jpg)
4. コミュニティ駆動: オープンソースでMicrosoftが主導していますが、他の多くの企業が貢献しています。プロジェクトはGitHub上で公開されており、誰でも参加できます。